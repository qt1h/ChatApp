# votre_app/routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

application = ProtocolTypeRouter({
    "websocket": URLRouter([path("chatrooms/chatroom/<int:chatroom_id>/", ChatConsumer.as_asgi()),]
    ),
})
