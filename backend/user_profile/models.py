from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='assets/user_images/')