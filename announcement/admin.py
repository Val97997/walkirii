from django.contrib import admin
from django.utils.html import format_html
from .models import Announcement, AnnouncementPhoto

class AnnouncementPhotoInline(admin.TabularInline):
    model = AnnouncementPhoto
    extra = 5  # Number of extra image fields to display

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    inlines = [AnnouncementPhotoInline]
    list_display = ["title", "author", "created_date"]
    list_display_links = ["title", "created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]

@admin.register(AnnouncementPhoto)
class AnnouncementPhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'announcement', 'display_image', 'uploaded_at']
    list_filter = ['uploaded_at']

    def display_image(self, obj):
        return format_html('<img src="{}" width="175px" height="125px" />', obj.image.url)

    display_image.short_description = 'Image'


