from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username','email','password')

    def validate_email(self, value):# Email unique hona chahiye,Same email se multiple accounts ban sakte hain isliaye ye function lagega
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user
class LoginSerializer(serializers.Serializer):
    email= serializers.EmailField(required=True)
    password = serializers.CharField(required=True,write_only=True)
