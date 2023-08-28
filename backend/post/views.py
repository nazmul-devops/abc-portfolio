# Create your views here.
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

from django.shortcuts import render
# import requests

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
def frontend_html_view(request):
    html_file_path = '/Users/Nazmul Islam/DevOps/git/python-django/portfolio/frontend/index.html'
    with open(html_file_path, 'r') as f:
        content = f.read()
    return render(request, 'frontend_page.html', {'local_content': content})