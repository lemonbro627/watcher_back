from django.urls import path

from . import views

urlpatterns = [
    path('getNewVideo', views.get_video, name='video'),
    path('getNewPhoto', views.get_photo, name='photo'),
    path('getNewFeed', views.get_feed, name='feed'),
]