from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from post import views

urlpatterns = [
    path('', lambda request: HttpResponse("<h1 style='text-align: center; margin-top: 30px;'>Welcome To Django Simple Portfolio Webapp</h1>", content_type="text/html")),
    # path('', views.frontend_html_view, name='frontend_html_view'),
    path("admin/", admin.site.urls),
    path("api/", include('post.urls')),
    path("api/user/", include('user_profile.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# Customized Django Admin UI 
admin.site.site_header = "ABC Portfolio Admin"
admin.site.site_url = "http://127.0.0.1:5500/frontend/index.html"
admin.site.site_title = "ABC Portfolio Admin Portal"
admin.site.index_title = "Welcome to ABC Portfolio Portal"