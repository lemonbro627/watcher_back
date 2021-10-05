from django.urls import path

from . import views

urlpatterns = [
    path('getVideo', views.get_video, name='video'),
    path('getRunningString', views.get_running_string, name='running_string'),
]