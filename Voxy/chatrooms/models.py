from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    participants = models.ManyToManyField(User)  # Liste des personnes ayant accès à la chat room

    def __str__(self):
        return self.name

class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)  # La personne qui a posté le message
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)  # La chat room à laquelle le message est associé

    def __str__(self):
        return f"{self.sender.username} - {self.content[:50]}"

    class Meta:
        ordering = ['timestamp']
