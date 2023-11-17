import os
from django.forms import ValidationError
from django.shortcuts import render, redirect,get_object_or_404
from .models import Announcement, AnnouncementPhoto
from django.contrib import messages
from .forms import AnnouncementForm
from .decorators import is_instructor
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q
from django.contrib.auth.decorators import login_required

#from . import candy

# Create your views here.


def react_app(request):
    return render(request, 'html/shop.html')



def applyInstructor(request):

    return render(request, "html/instructorApplyForm.html")


def contact(request):

    return render(request, "html/contact.html")


def index(request):

    return render(request, "html/index.html")


def about(request):

    return render(request, "html/about.html")

def announcement_detail(request, announcement_id):
    announcement = get_object_or_404(Announcement, pk=announcement_id)
    return render(request, 'html/announcement_detail.html', {'announcement': announcement})

@login_required
def delete_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    
    # Check if the user is the author
    if request.user == announcement.author:
        # Delete associated image files from media folder
        for photo in announcement.announcement_photos.all():
            if os.path.exists(photo.image.path):
                os.remove(photo.image.path)
        
        announcement.delete()
        messages.success(request, 'Announcement deleted successfully.')
    else:
        messages.error(request, 'You do not have permission to delete this announcement.')

    return redirect('announcement:announcements')  # Redirect to announcements page


""" @login_required
def delete_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    
    # Check if the user is the author and an instructor
    if request.user == announcement.author:
        announcement.delete()
        messages.success(request, 'Announcement deleted successfully.')
    else:
        messages.error(request, 'You do not have permission to delete this announcement.')

    return redirect('announcement:announcements')  # Redirect to announcements page """


def search_announcements(request):
    query = request.GET.get('query')
    results = []

    if query:
        results = Announcement.objects.filter(
            Q(title__icontains=query) | 
            Q(author__username__icontains=query) |
            Q(GeographicalLocation__icontains=query)
        )

    context = {'query': query, 'results': results}
    return render(request, 'html/searchAnnouncements.html', context)

def announcements(request):
    all_announcements = Announcement.objects.all()
    return render(request, "html/announcements.html", {'results': all_announcements})



def addAnnouncement(request):
    if request.method == "POST":
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            # Check if the user has already submitted an announcement
            existing_announcement = Announcement.objects.filter(author=request.user).first()

            if existing_announcement:
                messages.warning(request, 'You have already submitted an announcement.')
                return redirect("index")

            announcement = form.save(commit=False)
            announcement.author = request.user
            announcement.save()
            photos = request.FILES.getlist('photos')[:5]  # Limit to 5 photos

            for image in photos:
                photo = AnnouncementPhoto(announcement=announcement, image=image)
                photo.save()

            messages.info(request, 'The announcement has been successfully added.')
            return redirect("index")
    else:
        form = AnnouncementForm()

    return render(request, "html/addannouncement.html", {"form": form})







