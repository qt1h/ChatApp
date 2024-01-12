from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    participants = models.ManyToManyField(User, related_name='participant_chatrooms')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_chatrooms')
    deleted_messages = models.ManyToManyField('Message', related_name='deleted_in_chatrooms')
    def __str__(self):
        return self.name
    
    def delete_message(self, message_id):
        message = self.message_set.filter(id=message_id).first()
        if message:
            self.deleted_messages.add(message)
            return True
        return False

class Message(models.Model):
    content = models.CharField(max_length=1024)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
	
    def formatted_timestamp(self):
        local_time = timezone.localtime(self.timestamp)
        return local_time.strftime("%d/%m/%Y %H:%M:%S")
    
    def __str__(self):
        return f"{self.sender.username} - {self.content[:50]}"

    class Meta:
        ordering = ['-id']  # Tri par ordre décroissant d'ID
