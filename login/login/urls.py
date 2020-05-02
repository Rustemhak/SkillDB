from django.conf.urls import url
from django.contrib.auth import views as auth_views

from login import views
from login.forms import LoginForm, PasswordResetEmailForm, MySetPasswordForm

urlpatterns = [
    url(r'^login/', auth_views.LoginView.as_view(
        form_class=LoginForm,
        template_name='registration/login.html',
        authentication_form=LoginForm),
        name='login'),
    url(r'^profile/', views.ProfileView.as_view(),
        name='profile'),
    url(r'^logout/', auth_views.LogoutView.as_view(
        template_name='profile/profile.html', next_page=None),
        name='logout'),
    url(r'^reset_password/',
        auth_views.PasswordResetView.as_view(
            email_template_name='registration/reset_password_email.html',
            template_name='registration/reset_password.html',
            form_class=PasswordResetEmailForm,
            ), name='reset_password'),
    url(r'^password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset_password_confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.PasswordResetConfirmView.as_view(
        form_class=MySetPasswordForm,
        template_name='registration/reset_password_confirm.html'),
        name='reset_password_confirm'),
    url(r'^password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
