from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import User
from .serializers import LoginSerializer

class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        
        if user is not None:
            token = Token.objects.create(user=user)
            return Response({"Token": token.key})
        else:
            print("error")
            return Response(status=401)