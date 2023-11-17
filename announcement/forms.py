from django import forms
from .models import Announcement
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.core.files import File


class AnnouncementForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Instructor name *'}), required=True)
    title = forms.CharField(label='Title of the training session', widget=forms.TextInput(attrs={'placeholder': 'Enter title *'}), required=True)
    catchTitle = forms.CharField(label='Catch Title', widget=forms.TextInput(attrs={'placeholder': 'Brief description'}))
    content = forms.CharField(label='Exhaustive description', widget=forms.Textarea(attrs={'placeholder': 'Description *'}), required=True)
    GeographicalLocation = forms.CharField(label='Geographical location', widget=forms.TextInput(attrs={'placeholder': 'Location *'}), required=True)
    clientNumMax = forms.IntegerField(label='Client numbers', widget=forms.TextInput(attrs={'placeholder': 'Max Clients *'}), required=True)
    duration = forms.IntegerField(label='Duration')

    TIME_PERIOD_CHOICES = [
        ('Hours', 'Hours'),
        ('Days', 'Days'),
        ('Weeks', 'Weeks'),
        ('Months', 'Months'),
    ]
    time_period = forms.ChoiceField(label='Duration type', choices=TIME_PERIOD_CHOICES)

    BOOLEAN_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    food = forms.ChoiceField(label='Food', choices=BOOLEAN_CHOICES)
    sleepOrganisation = forms.ChoiceField(label='Sleep organization', choices=BOOLEAN_CHOICES)

    dates = forms.DateField(label='Start Date')
    to = forms.DateField(label='End Date')

    pricing = forms.DecimalField(label='Pricing', widget=forms.TextInput(attrs={'placeholder': 'Pricing *'}), required=True)

    photos = forms.FileField(
        label='Gallerie Import',
        widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}),
        required=False
    )

    def clean_photos(self):
        photo = self.cleaned_data.get('photos')  # Get the cleaned data for the photos field

        if photo:
            max_photo_size = 10 * 1024 * 1024  # 10 MB in bytes

            if photo.size > max_photo_size:
                raise ValidationError('Each photo should be less than 10MB.')

        return photo

    
    def clean_duration(self):
        duration = self.cleaned_data.get('duration')
        if duration < 0:
            raise forms.ValidationError('Duration must be a positive number.', code='invalid')
        return duration

    def clean_clientNumMax(self):
        max_clients = self.cleaned_data['clientNumMax']
        if max_clients < 1:
            raise forms.ValidationError('Client numbers cannot be less than 1.', code='invalid')
        return max_clients

    def clean_pricing(self):
        price = self.cleaned_data.get('pricing')
        if price < 0:
            raise forms.ValidationError('Price must be a positive number.', code='invalid')
        return price
    
    class Meta:
        model = Announcement
        fields = ['name', 'title', 'catchTitle', 'content', 'GeographicalLocation', 'clientNumMax', 'duration', 'time_period', 'food', 'sleepOrganisation', 'dates', 'to','pricing','photos']










