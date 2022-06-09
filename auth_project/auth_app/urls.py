from django.urls import path
from auth_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import (
    LoginForm,
    MypasswordChangeForm,
    MyPasswordResetForm,
    MysetPasswordForm
)

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
        
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    path('passwordchange/', auth_views.PasswordChangeView.as_view(
        template_name='app/passwordchange.html', form_class=MypasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(
        template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='app/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='app/password_reset_confirm.html', form_class=MysetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='app/password_reset_complete.html'), name='password_reset_complete'),

    path('userregistration/', views.UserRegistrationView.as_view(),
        name='userregistration'),

]
