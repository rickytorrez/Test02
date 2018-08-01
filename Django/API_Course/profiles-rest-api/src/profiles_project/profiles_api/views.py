from django.shortcuts import render

from rest_framework import viewsets                                             # Viewsets

from rest_framework.views import APIView
from rest_framework.response import Response                                    # Response object
from rest_framework import status                                               # Status contains a list of different HTTP status codes


from . import serializers                                                       # Import serializers.py module

class HelloAPIView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer                              # Tells Django to use serializer class

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [                                                          # List Variable
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})        # Response refers to the response imported from the rest_framework aboce
                                                                                # It must be passed a dictionary to return the response
                                                                                # The Response is a dictionary that is converted to JSON to be outputed
                                                                                # to the screen

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)             # Creates a serializer object with our HelloSerializer class and passes
                                                                                # in the data from the request.data attribute

        if serializer.is_valid():                                               # If the serializer is valid:
            name = serializer.data.get('name')                                  # Retrives the specific data inside the request.data, in this case, the name
            message = 'Hello {0}'.format(name)                                  # Creates a message passing the post name
            return Response ({'message': message})                              # Returns the message
        else:
            return Response(                                                    # Return the serializer error and HTTP error code
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):                                            # pk= Primary key
        """Handles updating an object."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object."""

        return Response({'method':'delte'})


class HelloViewSet(viewsets.ViewSet):                                           # Viewsets
    """TEST API ViewSet."""

    def list(self,request):                                                     # Equivalent to GET
        """Return a hello message."""
        a_viewset = [
            'Uses actions(list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs uring Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message':'Hello!', 'a_viewset':a_viewset})