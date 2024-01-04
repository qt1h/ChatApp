from django.shortcuts import render
from .models import ChatRoom
from .forms import MessageForm

def home_view(request):
    user = request.user
    accessible_chatrooms = ChatRoom.objects.filter(participants=user)
    message_form = MessageForm()

    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            chatroom_id = request.POST.get('chatroom_id')
            message_content = message_form.cleaned_data['message']
            if chatroom_id and message_content:
                chatroom = ChatRoom.objects.get(id=chatroom_id)
                Message.objects.create(content=message_content, sender=user, chat_room=chatroom)
                # Rediriger pour éviter le renvoi du formulaire lors du rechargement de la page
                return redirect('home')

    return render(request, 'chatroom.html', {'user': user, 'accessible_chatrooms': accessible_chatrooms, 'message_form': message_form})
