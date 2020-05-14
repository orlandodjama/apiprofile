from django.shortcuts import render
from rest_framework.views import APIView, Response
# Create your views here.

class HelloApiView(APIView):

    def get(self, request, format=None):

        an_apiview =[
            'Uses HTTP methods as function (get , post , patch, put, delete)',
            'it is similar to trad Django view',
            'give the control over logic',
            'is mapped manually to URLS'
        ]

        return Response({'message':'hello' , 'an_apiview': an_apiview})