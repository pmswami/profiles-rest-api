from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class HelloApiView(APIView):
    """Test API View"""
    
    serializer_class =serializers.HelloSerializer
    
    def get(self, request, format=None):
        """Returns  list of PIView Features"""
        an_apiview = [
            "Uses HTTP Methods as function (get, post, patch, put, delete)",
            "Is similar to traditional django view",
            "Gives you the most control over application logic",
            "Is mapped manually to URLs",
        ]
        return Response({"message":"Hello", "an_apiview":an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message':message},status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializers.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def put(self, request, pk=None):
        """Handle updating and object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update on objects"""
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete Object from database"""
        return Response({'method':'DELETE'})
    
class HelloViewSet(viewsets.ViewSet):
    """Testing api views set"""
    
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello Message."""
        a_viewset=[
            'uses actions such as create , retrieve, update, partial_update',
            'automatically maps urls using routers',
            'provides more functionality with less code',
        ]
        
        return Response({"message": "Hello!", "a_viewset": a_viewset})
    
    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'hello {name}!'
            return Response({"message": message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
        
    def retrieve(self, request, pk=None):
        """handle getting an individual obj by its id"""
        return Response({"http_method ": "GET"})
    
    def update(self, request,pk=None ):
        """handling the full update of  existing data in db"""
        return Response ({"http_method" : "PUT"})
    
    def partial_update(self, request, pk= None):
        """Handle updating part of an object"""
        return Response ({ "http_method":"PATCH"})
    
    def destroy(self, request, pk=None):
        """Handle removing of an object"""
        return Response({ "http_method":"DELETE"})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes =(permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "email", )

class UserLoginApiView(ObtainAuthToken):
    """Handle Creating user Authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    