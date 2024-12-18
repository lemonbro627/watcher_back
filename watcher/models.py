from django.utils import timezone
from django.db import models



# Create your models here.

class VideoPanel(models.Model):
    class Meta:
        verbose_name = 'ВидеоПанель'
        verbose_name_plural = 'ВидеоПанели'

    title = models.CharField(max_length=32, verbose_name='Имя панели')
    IP = models.GenericIPAddressField(verbose_name='IP адрес', null=False, blank=False)

    def __str__(self):
        return f'{self.title} ({self.IP})'


class Video(models.Model):
    VideoFreq = [
        ('VERY_HIGH', 'Очень часто'),
        ('HIGH', 'Часто'),
        ('MID', 'Средне'),
        ('LOW', 'Редко'),
        ('VERY_LOW', 'Очень редко')]

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    title = models.CharField(max_length=64, verbose_name='Заголовок')
    start_date = models.DateField(verbose_name='Дата начала показа (включая)', default=timezone.now,
                                  null=False, blank=False, editable=True)
    end_date = models.DateField(verbose_name='Дата конца показа (включая)', default=timezone.now,
                                null=False, blank=False, editable=True)
    freq = models.CharField(max_length=9, choices=VideoFreq, default='MID', verbose_name='Частота показа', null=False,
                            blank=False)
    video_url = models.URLField(verbose_name='Ссылка на видео (только прямые ссылки на mp4)', null=True, blank=False)
    panels = models.ManyToManyField(verbose_name='На каких панелях отображать?', to=VideoPanel, related_name='панель')
    is_enabled = models.BooleanField(verbose_name='Показывать?', default=True, null=False, blank=False)
    is_fullscreen = models.BooleanField(verbose_name='Разворачивать на весь экран?', default=False, null=False,
                                        blank=False)
    for_rector = models.BooleanField(verbose_name='Для ректора?', default=False, null=False, blank=False)

    def __str__(self):
        return self.title
