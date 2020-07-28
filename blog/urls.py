from django.urls import path
from .views import home, new_post, post_detail
urlpatterns = [
    path('', home, name='home'),
    path('new-post/', new_post, name='new-post'),
    path('<slug>/', post_detail, name='post-detail'),
]
