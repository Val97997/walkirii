from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
import pycountry


ALL_LANGUAGES = [(lang.alpha_2, lang.name)
                 for lang in pycountry.languages if hasattr(lang, "alpha_2")]


def user_directory_path(instance, filename):
    return 'users/avatars/{0}/{1}'.format(instance.user.id, filename)

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pseudonym = models.CharField(max_length=50, default='', blank=True)
    gender = models.CharField(
        max_length=6,
        default='MALE',
        blank=True,
        choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')]
    )
    twitter = models.CharField(max_length=100, default='', blank=True)
    instagram = models.CharField(max_length=100, default='', blank=True)
    linkedin = models.CharField(max_length=100, default='', blank=True)
    phone_number = PhoneNumberField(help_text='Required')
    youtube = models.CharField(max_length=100, default='', blank=True)
    language = models.CharField(max_length=2, choices=ALL_LANGUAGES, blank=True)
    secondlanguage = models.CharField(
        max_length=2, choices=ALL_LANGUAGES, verbose_name="Second Language", help_text='Optional', blank=True)
    location = models.CharField(max_length=50, help_text='Required')
    avatar = models.ImageField(upload_to=user_directory_path, default='avatar.jpg', blank=True, null=True)
    birthday = models.DateField(verbose_name="Birthday", null=True, blank=True)
    presentation = models.TextField(blank=True, verbose_name="Short Presentation")
    last_formation = models.CharField(max_length=100, default='', blank=True, verbose_name="Latest Animated Training")

    def clean_avatar(self):
        if self.avatar:
            if self.avatar.size > 2 * 1024 * 1024:
                raise ValidationError(_('Avatar file size should be less than 2MB.'))
        return self.avatar

    def __str__(self):
        return self.user.username
