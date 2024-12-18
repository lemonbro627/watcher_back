# Generated by Django 3.2.7 on 2024-12-18 11:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0004_auto_20211005_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Имя панели')),
                ('IP', models.GenericIPAddressField(verbose_name='IP адрес')),
            ],
            options={
                'verbose_name': 'ВидеоПанель',
                'verbose_name_plural': 'ВидеоПанели',
            },
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AddField(
            model_name='video',
            name='for_rector',
            field=models.BooleanField(default=False, verbose_name='Для ректора?'),
        ),
        migrations.AddField(
            model_name='video',
            name='is_fullscreen',
            field=models.BooleanField(default=False, verbose_name='Разворачивать на весь экран?'),
        ),
        migrations.AlterField(
            model_name='video',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2025, 1, 1, 11, 51, 31, 203365, tzinfo=utc), verbose_name='Дата конца паказа(включая)'),
        ),
        migrations.AlterField(
            model_name='video',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2024, 12, 18, 11, 51, 31, 203365, tzinfo=utc), verbose_name='Дата начала показа (включая)'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_url',
            field=models.URLField(null=True, verbose_name='Ссылка на видео (только прямые ссылки на mp4)'),
        ),
        migrations.AddField(
            model_name='video',
            name='panels',
            field=models.ManyToManyField(related_name='панель', to='watcher.VideoPanel', verbose_name='На каких панелях отображать?'),
        ),
    ]