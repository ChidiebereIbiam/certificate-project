from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('<int:pk>/profile', views.ProfilePageView.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile', views.UpdateProfileView.as_view(), name='update_profile'),
    path('password/', views.PasswordsChangeView.as_view(template_name='registration/change-password.html'), name="change-password"),
    path('password_success/', views.Password_Success, name='password_success'),
]