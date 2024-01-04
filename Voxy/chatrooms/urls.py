from django.urls import path
from . import views

app_name = 'chatrooms'
urlpatterns = [
    path('chatroom/', views.home_view, name='chatroom'),
]