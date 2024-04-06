from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from .consumers import PostConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/posts/', PostConsumer.as_asgi()),
    ]),
})
