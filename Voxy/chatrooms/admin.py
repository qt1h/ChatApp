from django.contrib import admin
from .models import ChatRoom, Message

admin.site.register(ChatRoom)
admin.site.register(Message)

class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('name')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('content', 'sender', 'timestamp', 'chat_room')
    list_filter = ('chat_room')
    search_fields = ('content', 'sender__username', 'chat_room__name')
