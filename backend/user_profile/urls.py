from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *



urlpatterns = [
    path('', UserList.as_view(), name='user_list'),
]
