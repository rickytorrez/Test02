from asgiref.sync import async_to_sync                                          # necessary modules to save our consumer
from channels.generic.websocket import WebsocketConsumer
import json                                                                     # import json module to transform data to JSON and vice-versa

from . import models                                                            # import models to save data

class NoteConsumer(WebsocketConsumer):
    def connect(self):                                                          # Connection method: defines what should happen once we establish a connection
        self.room_group_name = 'notes'                                          # In this case, we create a new room called notes

        async_to_sync(self.channel_layer.group_add)(
        self.room_group_name,
        self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):                                           # Disonnect method: close the room and the channel
        async_to_sync(self.channel_layer.group_discard)(
        self.room_group_name,
        self.channel_name
        )

    def receive(self, text_data):                                               # Receive method: Define what should happen when we receive data
        text_data_json = json.load(text_data)
        title = text_data_json['title']                                         # Extract everything we need from the text data
        content = text_data_json['content']
        id = text_data_json['id']

        note = models.Note.objeccts.get(pk=id)                                  # We use the model to find the model by its id
        note.title = title                                                      # Update its content
        note.content = content
        note.save()                                                             # save it to the database

        async_to_sync(self.channel_layer.group_send)(                           # Also sync the data between the channel group
        self.room_group_name,
            {
            'type':'add_note',                                                  # Create a new channel group and pass in the type, title, content
            'title': title,
            'content': content,
            'id': id
            }
        )

    def add_note(self, event):                                                  # Add note method: Accepts the event, we extract everything from this event
        title = event['title']                                                  # Title, content, id
        content = event['content']
        id = event['id']
        self.send(text_data=json.dumps({                                        # Send extracted data to the listening channel
            'title': title,
            'content': content,
            'id': id
        }))
