from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView, Response, status
from . import serializers

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

    def list(self, request):

        a_viewset =[
            'Uses actions (list, create,retrueve)',
            'automaticcally maps to URLS using Routers',
            'provide more functionnality for less code',
            
        ]

        return Response({'message':'hello' , 'a_viewset': a_viewset})
