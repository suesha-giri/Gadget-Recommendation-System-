from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns=[
    path("register", views.register, name='register'),
    path("loginPage", views.loginPage, name='loginPage'),
    path("logoutUser", views.logoutUser, name='logoutUser'),
    path("password-reset",auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path("password-reset/done",auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path("password-reset-complete",auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path("profile",views.profile,name='profile'),
    path("edit", views.edit, name='edit')
    

]