import os
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.conf import settings
from user.models import Account
from .forms import AccountForm, RegistrationForm
from .tokens import account_activation_token
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from announcement.decorators import is_instructor
from django.contrib.auth.decorators import user_passes_test
from django.core.files.storage import FileSystemStorage


def profile(request):
    # Common profile view for both normal users and instructors
    if is_instructor(request.user):
        return render(request, 'html/profileInstructor.html', {'section': 'profile'})
    else:
        return render(request, 'html/profile.html', {'section': 'profile'})


def edit(request):
    try:
        account = request.user.account
    except Account.DoesNotExist:
        account = Account(user=request.user)
        account.save()

    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES, instance=account)
        if form.is_valid():
            profile = form.save(commit=False)

            # Handle the avatar upload and saving
            if 'avatar' in request.FILES:
                uploaded_avatar = request.FILES['avatar']
                profile.avatar = uploaded_avatar

            elif 'clear_avatar' in request.POST:
                profile.avatar.delete()  # Clear the current avatar

            # Update the first name and last name from the form data
            request.user.first_name = form.cleaned_data.get('first_name', '')
            request.user.last_name = form.cleaned_data.get('last_name', '')
            request.user.save()

            # Save the account profile
            profile.save()

            messages.success(request, 'Profile updated successfully!')
            return redirect('index')
    else:
        form = AccountForm(instance=account)

    if is_instructor(request.user):
        return render(request, 'html/updateInstructor.html', {'form': form, 'section': 'update'})
    else:
        return render(request, 'html/update.html', {'form': form})


@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user

        avatar_path = user.account.avatar.path

        user.delete()

        if avatar_path and os.path.exists(avatar_path):
            os.remove(avatar_path)

        messages.success(
            request, 'Your account and avatar have been deleted successfully!')
        return redirect('index')

    return render(request, 'html/confirm_delete_account.html')


def register(request):
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.first_name = registerForm.cleaned_data['first_name']
            user.last_name = registerForm.cleaned_data['last_name']
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('html/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)

            messages.success(
                request, 'Your account has been created successfully. Please check your email to activate your account.')
            return redirect("index")  # redirect to homepage
    else:
        registerForm = RegistrationForm()

    return render(request, "html/register.html", {'form': registerForm})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('user:login')
    else:
        return render(request, 'html/account_activation_invalid.html')


def logoutUser(request):
    logout(request)
    return redirect('user:login')
