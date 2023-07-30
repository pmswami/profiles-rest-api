from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Returns  list of PIView Features"""
        an_apiview = [
            "Uses HTTP Methods as function (get, post, patch, put, delete)",
            "Is similar to traditional django view",
            "Gives you the most control over application logic",
            "Is mapped manually to URLs",
        ]
        return Response({"message":"Hello", "an_apiview":an_apiview})
    
