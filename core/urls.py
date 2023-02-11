from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('certificate/', views.certificate_detail, name='certificate_detail')
]