from django.urls import path
from . import views

app_name = 'chatrooms'
urlpatterns = [
    path('chatroom/', views.home_view, name='chatroom'),
    path('chatroom/<int:chatroom_id>/', views.home_view, name='chatroom'),
    path('create_chatroom/', views.create_chatroom, name='create_chatroom'),
    path('delete/<int:chatroom_id>/', views.delete_chatroom, name='delete_chatroom'),
    path('rafraichir_messages/<int:chatroom_id>/', views.rafraichir_messages, name='rafraichir_messages'),
    path('send_message/', views.send_message, name='send_message'),
    path('add_user/<int:chatroom_id>/', views.add_user_to_chatroom, name='add_user_to_chatroom'), 
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),

   
    
]