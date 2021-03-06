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
    )
    list_display_links = (
        'title',
    )
    list_editable = (
        'is_enabled',
    )


admin.site.register(Video, VideoAdmin)
