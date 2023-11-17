from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm, PwdResetForm,PwdResetConfirmForm
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "user"

urlpatterns = [

    path('password_reset/',auth_views.PasswordResetView.as_view(form_class=PwdResetForm),name='password_reset'),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html',form_class=PwdResetConfirmForm),name='password_reset_confirm'),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
 
    path('register/',views.register, name = "register" ),
    path('login/', auth_views.LoginView.as_view(template_name="html/login.html",
                                               authentication_form=UserLoginForm), name='login'),                                        
    path('logout/',views.logoutUser, name = "logout" ),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit, name='edit'),
    path('activate/<slug:uidb64>/<slug:token>)/',
         views.activate, name='activate'),
    path('delete_account/', views.delete_account, name='delete_account'),         

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
