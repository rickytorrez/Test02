from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)                                 # Describes the fields as class variables

class UserProfileSerializer(serializers.ModelSerializer):                       # Model serializer, designed to be used with Django Model
    """A serializer for our user profile objects."""

    class Meta:                                                                 # Meta class tells Django what fields we want to take from our model
        model = models.UserProfile                                              # It tells django that the serializer will user the UserProfile model
        fields = ('id','email','name','password')                               # Tell django what fields in our model we want to use with our serializer
        extra_kwargs = {'password': {'write_only': True}}                       # Defines extra keywords for our fields, tells django special attributes we
                                                                                # want to allow to these fields, we want the password to be write only

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
