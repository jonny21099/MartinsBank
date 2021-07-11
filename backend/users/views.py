from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response

from .models import User

from .serializer import UserSerializer


# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer



