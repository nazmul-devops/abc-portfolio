from django.contrib import admin

from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = [u.name for u in User._meta.fields]

admin.site.register(User, UserAdmin)
