# from django.shortcuts import render
from .models import *
from random import choice
from json import dumps
from django.http import HttpResponse
import datetime
import feedparser


BASE_URL = 'http://127.0.0.1:8000'
# Create your views here.

freq_list = {
    'VERY_HIGH': 5,
    'HIGH': 4,
    'MID': 3,
    'LOW': 2,
    'VERY_LOW': 1
}


def get_video(request):
    response = {'url': 'https://media.psu.ru/www.psu.ru/video/infopanel/2021/univer-2021.mp4', 'is_fullscreen': 'false'}

    ip = request.META.get('HTTP_X_REAL_IP')
    print(f'Client IP addr: {ip}')
    video_list = Video.objects.all()
    videos_by_panels = []
    videos_for_rector = []
    for video in video_list:
        allowed = [panel.IP for panel in video.panels.all()]
        if video.is_enabled and video.start_date <= datetime.date.today() <= video.end_date and ip in allowed:
            for x in range(0, freq_list[video.freq]):
                videos_by_panels.append({"url": video.video_url, "is_fullscreen": video.is_fullscreen})
        if video.is_enabled and video.start_date <= datetime.date.today() <= video.end_date and video.for_rector:
            videos_for_rector.append({"url": video.video_url, "is_fullscreen": True})
    try:
        if ip == '10.10.50.101' and len(videos_for_rector) > 0:
            response = choice(videos_for_rector)
        else:
            response = choice(videos_by_panels)
    except:
        pass
    print(f'Client: {ip}, Response: {response}')
    return HttpResponse(dumps(response))


def get_news_of_day(request):
    response = {'string': 'null'}
    d = feedparser.parse('http://www.psu.ru/news?format=feed&type=rss')
    feeds = [d.entries[0].title, d.entries[1].title, d.entries[2].title]
    response['string'] = choice(feeds)
    return HttpResponse(dumps(response))


def status(request):
    return HttpResponse('ok')


def index(request):
    ip = request.META.get('HTTP_X_REAL_IP')
    response = ip
    return HttpResponse(response)