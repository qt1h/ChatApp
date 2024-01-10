from django.shortcuts import render, redirect, get_object_or_404
from .models import ChatRoom, Message
from .forms import MessageForm
from manage_emojis.models import Emoji

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
        # If no specific chatroom is requested, use the first accessible chatroom as the default
        chatroom = accessible_chatrooms.first()
        if chatroom is None:
            # Redirect to a page indicating that no accessible chatrooms are available
            return render(request, 'chatroom.html')
        
        
        return redirect('chatrooms:chatroom', chatroom_id=chatroom.id)

    # Retrieve the chatroom and its messages
    chatroom = get_object_or_404(ChatRoom, id=chatroom_id)
  
    messages = chatroom.message_set.all()
    return render(request, 'chatroom.html', {'user': user, 'accessible_chatrooms': accessible_chatrooms, 'message_form': message_form, 'chatroom': chatroom,'emojis': emojis, 'messages': messages})


def create_chatroom(request):
    if request.method == 'POST':
        chatroom_name = request.POST.get('chatroom_name')
        # Ajoutez d'autres champs ou validations si nécessaire

        chatroom = ChatRoom.objects.create(name=chatroom_name)
        chatroom.participants.add(request.user)  # Ajoutez le créateur du salon comme participant
        return redirect('chatrooms:chatroom', chatroom_id=chatroom.id)