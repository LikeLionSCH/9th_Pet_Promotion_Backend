from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from knox.models import AuthToken
from .models import User
from .serializers import LoginSerializer, UserSerializer

'''
class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        
        if user is not None:
            token = Token.objects.create(user=user)
            return Response({"Token": token.key})
        else:
            print("error")
            return Response(status=401)

class ProfileView(generics.RetrieveAPIView):
    def get(self, request):
        permission_classes = [
            permissions.IsAuthenticated,
        ]
        serializer_class = LoginSerializer

        def get_object(self):
            return Response(request.user)
'''

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
        })

class UserView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
