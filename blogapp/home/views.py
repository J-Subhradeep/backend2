from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BlogPost
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import BlogPostSerializer
# Create your views here.


class BlogPostView(APIView):
    def get(self, request, pk=None, format=None):
        blg = BlogPost.objects.all()
        if pk:
            blg = BlogPost.objects.get(pk=pk)
        serializers = BlogPostSerializer(blg, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
