from django.shortcuts import render, HttpResponse

from rest_framework import generics
from .models import *
from .serializers import UserSerializer

# Create your views here.

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

# def user_profile_home_view(request, *args, **kwargs):
#     return HttpResponse("<h1 style='text-align: center; margin-top: 30px;'>Welcome To Django User Profile.</h1>", content_type="text/html")
