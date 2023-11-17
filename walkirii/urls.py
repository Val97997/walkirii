
from django.contrib import admin
from announcement import views

from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name = "index"),
    path('about/', views.about,name = "about"),
    path('announcements/', include('announcement.urls')),
    path('user/', include('user.urls',namespace='users')),
    path('user/', include('django.contrib.auth.urls')),
    path('shop/', views.react_app, name='shop'),
    path('contact/', views.contact, name='contact'),
    path('apply/', views.applyInstructor, name='apply'),

    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

