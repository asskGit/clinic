from rest_framework import viewsets, status
from .models import User
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

