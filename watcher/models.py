from django.db import models
import datetime
# Create your models here.


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
    start_date = models.DateField(verbose_name='Дата начала показа (включая)', default=datetime.date.today(), null=False, blank=False, editable=True)
    end_date = models.DateField(verbose_name='Дата конца паказа(включая)', default=datetime.date.today(), null=False, blank=False, editable=True)
    freq = models.CharField(max_length=9, choices=VideoFreq, default='MID', verbose_name='Частота показа', null=False, blank=False)
    video_url = models.URLField(verbose_name='Ссылка на видео', null=True, blank=False)
    is_enabled = models.BooleanField(verbose_name='Показывать?', default=True, null=False, blank=False)

    def __str__(self):
        return self.title


class Photo(models.Model):
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    title = models.CharField(max_length=64, verbose_name='Заголовок')
    photo = models.FileField(verbose_name='Картинка', upload_to='', null=True, blank=False)
    text_before = models.CharField(max_length=128, verbose_name='Текст над картинкой (128 символов максимум)', null=True, blank=True)
    text_after = models.CharField(max_length=64, verbose_name='Текст под картинкой (64 символа максимум)', null=True, blank=True)
    is_enabled = models.BooleanField(verbose_name='Показывать?', default=True, null=False, blank=False)

    def __str__(self):
        return self.title

