from django.urls import path, include
from SnapGram.consumer import ChatConsumer

websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()),
]