from rest_framework import serializers
from .models import UserData
from django.contrib.auth.models import User

# Create a class
class booksSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = UserData
        fields = ["id", "name", "email"]
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
 