from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('<int:pk>/profile', views.ProfilePageView.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile', views.UpdateProfileView.as_view(), name='update_profile'),
    path('password/', views.PasswordsChangeView.as_view(template_name='registration/change-password.html'), name="change-password"),
    path('password_success/', views.Password_Success, name='password_success'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]