from rest_framework import serializers
from .models import BlogPost
from django.contrib.auth.models import User


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'desc', 'owner_name', 'date', 'type']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
