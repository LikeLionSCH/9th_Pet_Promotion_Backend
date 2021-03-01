from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import ProfileSerializer

'''
# Create your views here.
class ProfileView(APIView):
    def get(self, request):
        serializer = ProfileSerializer(auth)
        print(serializer)
        return Response(serializer.data, status=200)
'''