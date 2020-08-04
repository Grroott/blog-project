from django.urls import path
from .views import home, new_post, post_detail, bookmark_post, like_post
urlpatterns = [
    path('', home, name='home'),
    path('new-post/', new_post, name='new-post'),
    path('<slug>/', post_detail, name='post-detail'),
    path('<slug>/bookmark-post/', bookmark_post, name='bookmark-post'),
    path('<slug>/like-post/', like_post, name='like-post'),
]
