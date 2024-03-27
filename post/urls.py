from django.urls import path
from .views import search_post

urlpatterns = [
    path('search/', search_post, name='search_post'),
]