from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password"
        ]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value
    
    def validate_useraname(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value
    
    def create(self, validated_data):
        return User.objects.create_user(
            username = validated_data["username"],
            email = validated_data['email'],
            password = validated_data['password']
        )
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            username = username,
            password = password
        )

        if not user:
            raise serializers.ValidationError("Invalid Username or Password")

        attrs['user'] = user
        return attrs
    