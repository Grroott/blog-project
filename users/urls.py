from django.urls import path
from .views import profiles

urlpatterns = [

    path('<str:username>/', profiles, name='profile'),

 ]