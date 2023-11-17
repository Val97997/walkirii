import os
from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from django.core.exceptions import ValidationError  
from phonenumber_field.modelfields import PhoneNumberField
from django.forms.fields import EmailField  
from django.forms.forms import Form  
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm
from .models import Account
from django.utils.translation import gettext_lazy as _



class BirthdayInput(forms.DateInput):
    input_type = 'date'
    template_name = 'django/forms/widgets/date.html'

    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs['placeholder'] = 'YYYY-MM-DD'
        super().__init__(attrs=attrs)

    def format_value(self, value):
        if value is None:
            return ''
        return value.strftime('%Y-%m-%d')



class AccountForm(forms.ModelForm):
    presentation = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 10, 'placeholder': 'Une présentation rapide'}),
        required=False,  # Make the field not required
    )
    last_formation = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Dernière formation animée'}),
        required=False,  # Make the field not required
    )

    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Prénom'}),
        required=True,  # Make the field required
        label='First Name',  # Set the label for the field
    )

    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Nom'}),
        required=True,  # Make the field required
        label='Last Name',  # Set the label for the field
    )

    class Meta:
        model = Account
        fields = ['pseudonym', 'gender', 'twitter', 'instagram', 'linkedin', 'phone_number', 'youtube', 'language', 'secondlanguage', 'location', 'avatar', 'birthday', 'last_formation']
        labels = {
            'pseudonym': _('Pseudonym'),
            'gender': _('Gender'),
            'twitter': _('Twitter'),
            'instagram': _('Instagram'),
            'linkedin': _('LinkedIn'),
            'phone_number': _('Phone Number'),
            'youtube': _('YouTube'),
            'language': _('Language'),
            'secondlanguage': _('Second Language'),
            'location': _('Location'),
            'avatar': _('Avatar'),
            'birthday': _('Birthday'),
            'last_formation': _('Dernière formation animée'),
            'last_name': 'Last Name',  # Set the label for the last_name field
            'first_name': 'First Name',  # Set the label for the first_name field
        }
        widgets = {
            'location': forms.TextInput(attrs={'placeholder': 'City, Country'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Contact number'}),
            'avatar': forms.ClearableFileInput(),
            'birthday': forms.DateInput(format='%m/%d/%Y', attrs={'placeholder': 'date de naissance mm/dd/yyyy'}),
           
    
        }

    phone_number = PhoneNumberField(blank=True, null=True)
    birthday = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y', attrs={'placeholder': 'mm/dd/yyyy'}),
        input_formats=['%m/%d/%Y'],
    )
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'placeholder': 'Adresse mail'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].initial = self.instance.user.email

    def clean(self):
        cleaned_data = super().clean()
        clear_avatar = cleaned_data.get('clear_avatar', False)

        if clear_avatar:
            cleaned_data['avatar'] = None

        return cleaned_data


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))

class PwdChangeForm(PasswordChangeForm):

    old_password = forms.CharField(
        label='Old Password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Old Password', 'id': 'form-oldpass'}))
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))
    


    
class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        test = User.objects.filter(email=email)
        if not test:
            raise forms.ValidationError(
                'Unfortunatley we can not find that email address')
        return email


    
class RegistrationForm(forms.ModelForm):

    username = forms.CharField(
        label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
        'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)
    
    
 
  
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name','last_name')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email



    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password']  
        )  
        return user


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})
