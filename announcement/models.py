from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.forms import ValidationError


def announcement_photos_directory_path(instance, filename):
    slug = slugify(instance.announcement.title)
    return f'announcements/{slug}/{filename}'


class AnnouncementPhoto(models.Model):
    announcement = models.ForeignKey(
        "announcement.Announcement", on_delete=models.CASCADE, related_name='announcement_photos')
    image = models.ImageField(upload_to=announcement_photos_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for {self.announcement.title}"


class Announcement(models.Model):
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    catchTitle = models.CharField(max_length=50, verbose_name="Catch Title")
    content = RichTextField()
    GeographicalLocation = models.CharField(
        max_length=50, verbose_name="Geographical Location")
    clientNumMax = models.IntegerField(verbose_name="Max Clients", null=True)
    duration = models.IntegerField(default=0)

    TIME_PERIOD_CHOICES = [
        ('Hours', 'Hours'),
        ('Days', 'Days'),
        ('Weeks', 'Weeks'),
        ('Months', 'Months'),
    ]
    time_period = models.CharField(
        max_length=30, choices=TIME_PERIOD_CHOICES, blank=True, null=True)

    BOOLEAN_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    food = models.CharField(
        max_length=3, choices=BOOLEAN_CHOICES, default='No')
    sleepOrganisation = models.CharField(
        max_length=3, choices=BOOLEAN_CHOICES, default='No', verbose_name="Sleep Organisation")

    dates = models.DateField(verbose_name="Dates from", blank=True, null=True)
    to = models.DateField(verbose_name="To", blank=True, null=True)

    pricing = models.PositiveIntegerField(default=0, verbose_name="Price")
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Creation Date")


    def __str__(self):
        return self.title
