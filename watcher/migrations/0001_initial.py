# Generated by Django 3.2.7 on 2021-10-04 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Заголовок')),
                ('photo_url', models.URLField(null=True, verbose_name='Ссылка на фото')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Заголовок')),
                ('start_date', models.DateField(auto_now=True, verbose_name='Дата начала показа')),
                ('end_date', models.DateField(auto_now=True, verbose_name='Дата конца паказа')),
                ('freq', models.CharField(choices=[('VERY_HIGH', 'Очень часто'), ('HIGH', 'Часто'), ('MID', 'Средне'), ('LOW', 'Редко'), ('VERY_LOW', 'Очень редко')], default='1', max_length=9, verbose_name='Частота показа')),
                ('video_url', models.URLField(null=True, verbose_name='Ссылка на видео')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Показывать?')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
    ]
