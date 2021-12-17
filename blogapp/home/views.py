from django.shortcuts import render
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BlogPost
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import BlogPostSerializer
# Create your views here.

#harry: ##HHHH@12345

class UserView(APIView):
    def get(self, request, pk=None, format=None):
        blg = BlogPost.objects.all()
        if pk:
            blg = BlogPost.objects.get(pk=pk)
        serializers = BlogPostSerializer(blg, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        user = User.objects.create_user(username, email, password)

        return Response({
            'message': 'OK'
        })        