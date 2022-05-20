# Create your views here.
 
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserData
from .serializers import booksSerializer
 
 
class booklist(APIView):
 
    def get(self,request):
        book1 = UserData.objects.all()
        serializer = booksSerializer(book1, many= True)
        return Response(serializer.data,status=status.HTTP_200_OK) # Return JSON
 
    def post(self):
        pass