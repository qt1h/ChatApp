from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # Import login_required decorator
from .models import ChatRoom, Message
from .forms import MessageForm
from django.contrib.auth.models import User
from manage_emojis.models import Emoji
from django.contrib import messages
from django.http import JsonResponse, HttpResponseBadRequest

@login_required(login_url='users:login')  # Specify the login URL
def home_view(request, chatroom_id=None):
    user = request.user
    accessible_chatrooms = ChatRoom.objects.filter(participants=user)
    message_form = MessageForm()
    emojis = Emoji.objects.all()
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            chatroom_id = message_form.cleaned_data.get('chatroom_id')
            message_content = message_form.cleaned_data['message']
            if chatroom_id and message_content:
                chatroom = ChatRoom.objects.get(id=chatroom_id)
                Message.objects.create(content=message_content, sender=user, chat_room=chatroom)
                return redirect('chatrooms:chatroom', chatroom_id=chatroom_id)

    if chatroom_id is None:
        chatroom = accessible_chatrooms.first()
        if chatroom is None:
            return render(request, 'chatroom.html')

        return redirect('chatrooms:chatroom', chatroom_id=chatroom.id)

    chatroom = get_object_or_404(ChatRoom, id=chatroom_id)
    messages = chatroom.message_set.all()
    
    # Format timestamps before passing them to the template
    formatted_messages = [
        {
            'id': msg.id,
            'sender': msg.sender.username,
            'content': msg.content,
            'timestamp': msg.formatted_timestamp(),
            'is_deleted':msg.is_deleted,# Use formatted_timestamp method
        }
        for msg in messages
    ]

    return render(request, 'chatroom.html', {'user': user, 'accessible_chatrooms': accessible_chatrooms, 'message_form': message_form, 'chatroom': chatroom, 'emojis': emojis, 'messages': formatted_messages})

@login_required
def delete_chatroom(request, chatroom_id):
    chatroom = get_object_or_404(ChatRoom, id=chatroom_id, creator=request.user)
    chatroom.delete()
    return redirect('chatrooms:chatroom')

@login_required
def create_chatroom(request):
    if request.method == 'POST':
        chatroom_name = request.POST.get('chatroom_name')
        # Ajoutez d'autres champs ou validations si nécessaire

        chatroom = ChatRoom.objects.create(name=chatroom_name ,creator=request.user)
        chatroom.participants.add(request.user)  # Ajoutez le créateur du salon comme participant

        return redirect('chatrooms:chatroom', chatroom_id=chatroom.id)
@login_required
def add_user_to_chatroom(request, chatroom_id):
    chatroom = get_object_or_404(ChatRoom, id=chatroom_id)

    # Check if the current user is the creator of the chatroom
    if request.user != chatroom.creator:
        messages.error(request, "Vous n'avez pas la permission d'ajouter des utilisateurs à ce salon.")
       	return redirect('chatrooms:chatroom', chatroom_id=chatroom.id)

    if request.method == 'POST':
        username = request.POST.get('username')

        # Check if the user with the given username exists
        try:
            user_to_add = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, f"Utilisateur avec le nom '{username}' non trouvé.")
            return redirect('chatrooms:chatroom', chatroom_id=chatroom.id)

        # Check if the user is already a participant in the chatroom
        if user_to_add in chatroom.participants.all():
            messages.warning(request, f"{user_to_add.username} est déjà un participant de ce salon.")
        else:
            # Add the user to the chatroom
            chatroom.participants.add(user_to_add)
            messages.success(request, f"{user_to_add.username} ajouté au salon avec succès.")

        return redirect('chatrooms:chatroom', chatroom_id=chatroom.id)
    else:
        # Handle GET requests if needed
        pass
@login_required
def delete_message(request, message_id):
    try:
        message = get_object_or_404(Message, id=message_id)
    except Message.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Message not found'}, status=404)

    # Vérifiez si l'utilisateur a la permission de supprimer le message
    if request.user == message.sender or request.user == message.chat_room.creator:
        message.is_deleted = True
        message.save()
        return JsonResponse({'status': 'success', 'message': 'Message marked as deleted'})
    else:
        return JsonResponse({'status': 'error', 'message': 'You do not have permission to delete this message'}, status=403)
@login_required
def send_message(request):
    if request.method == 'POST':
        chatroom_id = request.POST.get('chatroom_id')
        message_content = request.POST.get('message')

        if chatroom_id and message_content:
            chatroom = get_object_or_404(ChatRoom, id=chatroom_id)
            new_message = Message.objects.create(content=message_content, sender=request.user, chat_room=chatroom)

            messages = chatroom.message_set.filter(id__gt=new_message.id).order_by('-id')
            messages_data = [
                {
                    'id': msg.id,
                    'sender': msg.sender.username,
                    'content': msg.content,
                    'timestamp': msg.timestamp.strftime("%d/%m/%Y %H:%M:%S")
                }
                for msg in messages
            ]

            return JsonResponse({
                'status': 'success',
                'message': 'Message envoyé avec succès',
                'messages': messages_data,
                'last_message_id': new_message.id
            })
        else:
            return JsonResponse({'status': 'error', 'message': 'Des données requises sont manquantes'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée'})

@login_required
def rafraichir_messages(request, chatroom_id):
    chatroom = get_object_or_404(ChatRoom, id=chatroom_id)
    last_message_id = request.GET.get('last_message_id', 0)
    new_messages = chatroom.message_set.filter(id__gt=last_message_id).order_by('id')

    messages = [{'id': message.id, 'sender': message.sender.username, 'content': message.content, 'timestamp': message.timestamp} for message in new_messages]

    return JsonResponse({'messages': messages})

