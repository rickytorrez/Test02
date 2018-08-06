from rest_framework import serializers

from . import models

class NoteSerializer(serializers.ModelSerializer):
    """Converts our Note model into JSON response data with all the fields included."""                                      
    class Meta:
        model = models.Note
        fields = '__all__'
