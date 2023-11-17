from django.contrib import admin
from django.urls import path
from . import views
#from announcement import candy
from django.conf import settings
from django.conf.urls.static import static

app_name = "announcement"



urlpatterns = [

    #path('profile/',views.profile, name = "profile" ),
    path('create/',views.addAnnouncement, name = "create" ),
    path('',views.announcements, name = "announcements" ),
    path('search/',views.search_announcements, name = "search" ),
    path('announcement/<int:announcement_id>/', views.announcement_detail, name='announcement_detail'),
    path('announcement/<int:announcement_id>/delete/', views.delete_announcement, name='delete_announcement'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
