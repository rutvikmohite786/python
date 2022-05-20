from rest_framework import serializers
from .models import UserData
 
# Create a class
class booksSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = UserData
        fields = ["id", "name", "email"]
 