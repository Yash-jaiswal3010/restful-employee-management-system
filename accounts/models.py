from django.db import models
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import serializers
# Create your models here.
def validate_email(self, value):
    if User.objects.filter(email=value).exists():
        raise serializers.ValidationError("Email already exists")
    return value