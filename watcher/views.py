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
    video_list = Video.objects.all()
    videos = []
    response = {'url': 'https://media.psu.ru/www.psu.ru/video/infopanel/2021/univer-2021.mp4'}
    for video in video_list:
        if video.is_enabled and video.start_date <= datetime.date.today() <= video.end_date:
            for x in range(0, freq_list[video.freq]):
                videos.append(video.video_url)
    try:
        response['url'] = choice(videos)
    except:
        pass
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
    response = '0'
    return HttpResponse(response)