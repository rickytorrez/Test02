from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response                                    # Response object

class HelloAPIView(APIView):
    """Test API View."""

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
