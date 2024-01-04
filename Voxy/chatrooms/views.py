from django.shortcuts import render
from .models import ChatRoom
def home_view(request):
    user = request.user
    accessible_chatrooms = ChatRoom.objects.filter(participants=user)
    return render(request, 'chatroom.html', {'user': user, 'accessible_chatrooms': accessible_chatrooms})
