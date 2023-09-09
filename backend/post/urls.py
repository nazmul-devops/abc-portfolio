from django.urls import path
from .views import PostList, api_home_view

urlpatterns = [
    path('', api_home_view, name='api_home_view'),
    path('posts/', PostList.as_view(), name='post-list'),
]
