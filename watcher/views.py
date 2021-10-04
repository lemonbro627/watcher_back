from django.shortcuts import render
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


def get_photo(request):
    photo_list = Photo.objects.all()
    photos = []
    response = {
        'url': '',
        'text_before': '',
        'text_after': ''
    }
    for photo in photo_list:
        if photo.is_enabled:
            photos.append(photo)
    try:
        data = choice(photos)
        response['url'] = BASE_URL + data.photo.url
        response['text_before'] = data.text_before
        response['text_after'] = data.text_after
    except:
        pass
    return HttpResponse(dumps(response))


def get_feed(request):
    response = ""
    d = feedparser.parse('http://www.psu.ru/news?format=feed&type=rss')
    feed = choice(d.entries)
    response += "<h1 align=center>"+feed.title+"</h1>"
    response += "<h3><div style='margin-left: 16px;'>"+feed.description+"</div><h3>"
    return HttpResponse(response)
