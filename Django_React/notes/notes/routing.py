from django.urls import path
from . import consumers

websocket_urlpatterns = [                                                       # Websocket URL - path the client connects to
    path('ws/notes', consumers.NoteConsumer)
]
