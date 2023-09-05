from django.contrib import admin
from .models import *

# Register your models here.


class VideoAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
    )
    list_display = (
        'title',
        'start_date',
        'end_date',
        'freq',
        'video_url',
        'is_enabled',
        'is_fullscreen',
        'for_rector',
    )
    list_display_links = (
        'title',
    )
    list_editable = (
        'is_enabled',
        'is_fullscreen',
    )


class VideoPanelAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
    )
    list_display = (
        'title',
        'IP',
    )
    list_display_links = (
        'title',
    )


admin.site.register(Video, VideoAdmin)
admin.site.register(VideoPanel, VideoPanelAdmin)