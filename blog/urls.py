from django.urls import path
from .views import home, new_post
urlpatterns = [
    path('', home, name='home'),
    path('new-post/', new_post, name='new-post'),
]
