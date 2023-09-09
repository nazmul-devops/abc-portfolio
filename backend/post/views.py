# Create your views here.
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

from django.shortcuts import render, HttpResponse
# import requests

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
    
    
def frontend_html_view(request):
    html_file_path = '/Users/Nazmul Islam/DevOps/git/python-django/portfolio/frontend/index.html'
    with open(html_file_path, 'r') as f:
        content = f.read()
    return render(request, 'frontend_page.html', {'local_content': content})

def api_home_view(request, *args, **kwargs):
    return HttpResponse("<h1 style='text-align: center; margin-top: 30px;'>Welcome To Django Simple Portfolio API Homepage.</h1>", content_type="text/html")