from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("ws/<int:id>/", consumers.ChatConsumer.as_asgi()),
]