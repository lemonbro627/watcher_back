# from django.shortcuts import render
import logging

from .models import *
from random import choice
from json import dumps
from django.http import HttpResponse
from django.utils import timezone
import feedparser
from watcher.constants import FREQ_LIST, RECTOR_PANEL_IP

logger = logging.getLogger(__name__)

BASE_URL = 'http://127.0.0.1:8000'


def get_video(request):
    response = {'url': 'https://media.psu.ru/www.psu.ru/video/infopanel/2021/univer-2021.mp4', 'is_fullscreen': 'false'}

    ip = request.META.get('HTTP_X_REAL_IP')
    logger.info(f'Client real ip is {ip}')
    video_list = Video.objects.filter(is_enabled=True, start_date__lte=timezone.now(),
                                      end_date__gte=timezone.now(), panels__IP=ip)
    videos_by_panels = []
    videos_for_rector = []
    for video in video_list:
        for x in range(0, FREQ_LIST[video.freq]):
            videos_by_panels.append({"url": video.video_url, "is_fullscreen": video.is_fullscreen})
        if video.for_rector:
            videos_for_rector.append({"url": video.video_url, "is_fullscreen": True})
    try:
        if ip == RECTOR_PANEL_IP and len(videos_for_rector) > 0:
            response = choice(videos_for_rector)
        else:
            response = choice(videos_by_panels)
    except:
        pass
    logger.info(f'Client: {ip}, Response: {response}')
    return HttpResponse(dumps(response))


def get_news_of_day(request):
    ip = request.META.get("HTTP_X_REAL_IP")
    response = {'string': 'null'}
    d = feedparser.parse('http://www.psu.ru/news?format=feed&type=rss')
    feeds = [d.entries[i].title for i in range(0, 3)]
    response['string'] = choice(feeds)
    logger.info(f'Client: {ip}, Response: {response}')
    return HttpResponse(dumps(response), status=200)


def status(request):
    return HttpResponse('ok', status=200)


def index(request):
    ip = request.META.get('HTTP_X_REAL_IP')
    response = ip
    return HttpResponse(response, status=200)
