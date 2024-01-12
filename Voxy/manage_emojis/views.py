from django.shortcuts import render
from .models import Emoji

def emoji_list_view(request):
    emojis = Emoji.objects.all()
    return render(request, 'chatrooms/emojis.html', {'emojis': emojis})
