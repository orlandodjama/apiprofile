from django.shortcuts import render
from rest_framework import viewsets,filters
from rest_framework.views import APIView, Response, status
from rest_framework.authentication import TokenAuthentication
from . import serializers, models, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken



# Create your views here.

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
    

        an_apiview =[
            'Uses HTTP methods as function (get , post , patch, put, delete)',
            'it is similar to trad Django view',
            'give the control over logic',
            'is mapped manually to URLS'
        ]

        return Response({'message':'hello' , 'an_apiview': an_apiview})

    def post(self, request):

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello{0}".format(name)
            return Response({'message' : message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk=None):
        """update lobjet"""
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """update ce qui est donné"""
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self, request):

        a_viewset =[
            'Uses actions (list, create,retrueve)',
            'automaticcally maps to URLS using Routers',
            'provide more functionnality for less code',
            
        ]

        return Response({'message':'hello' , 'a_viewset': a_viewset})

    
    def create(self, request):

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello{0}".format(name)
            return Response({'message' : message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """handle getting an objects by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """handle updating an objects by its ID"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handle updating part an objects by its ID"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """handle removing an objects by its ID"""
        return Response({'http_method': 'DELETE'})

    
class UserProfileViewSet(viewsets.ModelViewSet):
    "handle creating and updating profiles"

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields =('name','email',)


class LoginViewSet(viewsets.ViewSet):
    """checks email and password and returns an auth token"""

    serializer_class = AuthTokenSerializer
    def create(self, request):
        """use the obtainauthtoken to validate and create a token"""

        return ObtainAuthToken().post(request)