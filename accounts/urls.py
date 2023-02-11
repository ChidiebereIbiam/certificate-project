from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('<int:pk>/profile', views.ProfilePageView.as_view(), name='profile_page'),
]