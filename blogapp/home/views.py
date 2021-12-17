from django.shortcuts import render
from rest_framework import response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import BlogPost
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import BlogPostSerializer, UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserView(APIView):
    def get(self, request, pk=None, format=None):
        queryset = User.objects.values('username', 'id')
        return Response(queryset, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        # username = data.get('username')
        # password = data.get('password')
        # email = data.get('email')
        serializers = UserSerializer(data=data, partial=True)
        # user = User.objects.create_user(username, email, password)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogPostApi(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
