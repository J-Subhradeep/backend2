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
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class UserView(APIView):
    def get(self, request, pk=None, format=None):
        queryset = User.objects.all()
        serializers = UserSerializer(queryset, many=True)

        return Response(serializers.data, status=status.HTTP_200_OK)

    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        serializers = UserSerializer(data=data, partial=True)
        if serializers.is_valid():
            user = User.objects.create_user(username, email, password)

            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogPostApi(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
