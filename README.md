## How to make a Django Rest Framework API in a Django Project

```py
python manage.py startapp user
```
- First create your django app with above command and write your model in models.py 

```py
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='assets/user_images/')
```
- Then register your model in admin.py 

```py
from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = [u.name for u in User._meta.fields]
```

- python manage.py makemigrations user
- python manage.py migragte 

- create a new file name serializers.py
```py
from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
```
- Then make changes in views.py file
```py
from rest_framework import generics
from .models import *
from .serializers import UserSerializer

# Create your views here.

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```
- And finally change your urls.py file

```py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *



urlpatterns = [
    path('', UserList.as_view(), name='user_list'),
]

python manage.py runserver
```