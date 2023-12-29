from django.urls import path
from . import views

app_name = 'chatrooms'
urlpatterns = [
    path('chatroom/', views.chatroom, name='chatroom'),
]