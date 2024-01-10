from django.urls import path
from . import views

app_name = 'chatrooms'
urlpatterns = [
    path('chatroom/', views.home_view, name='chatroom'),
    path('chatroom/<int:chatroom_id>/', views.home_view, name='chatroom'),
    path('create_chatroom/', views.create_chatroom, name='create_chatroom'),

]