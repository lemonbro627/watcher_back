from django.contrib import admin
from .models import *


# Register your models here.


class VideoAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
    )
    ordering = ["-is_enabled"]
    search_fields = ("title", "is_enabled", "for_rector", "is_fullscreen")
    list_display = (
        'title',
        'start_date',
        'end_date',
        'freq',
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
        'for_rector',
    )

    actions = [
        "enable_videos",
        "disable_videos",
        "disable_expired_videos",
    ]

    def enable_videos(self, request, queryset):
        for i in queryset:
            i.is_enabled = True
            self.message_user(request, f"Видео {i.title} включено")
        Video.objects.bulk_update(queryset, ["is_enabled"])

    enable_videos.short_description = (
        "Включить видео"
    )

    def disable_videos(self, request, queryset):
        for i in queryset:
            i.is_enabled = False
            self.message_user(request, f"Видео {i.title} выключено")
        Video.objects.bulk_update(queryset, ["is_enabled"])

    disable_videos.short_description = (
        "Выключить видео"
    )

    def disable_expired_videos(self, request, queryset):
        expired_videos = Video.objects.filter(is_enabled=True, end_date__lte=timezone.now())
        for i in expired_videos:
            i.is_enabled = False
            self.message_user(request, f"Видео {i.title} выключено в связи с истечением срока показа")
        Video.objects.bulk_update(expired_videos, ["is_enabled"])

    disable_expired_videos.short_description = (
        "Выключить истёкшие видео"
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
