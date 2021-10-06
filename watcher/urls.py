from django.urls import path

from . import views

urlpatterns = [
    path('getVideo', views.get_video, name='video'),
    path('getNewsOfDay', views.get_news_of_day, name='running_string'),
    path('', views.index, name='index'),
]