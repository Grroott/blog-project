from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('', include('blog.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)