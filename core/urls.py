from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('<id>/certificate/', views.certificate_detail, name='certificate_detail'),
    path('generate_certificate/', views.generate_certificate, name='generate_certificate'),
    path('manage_certificate/', views.manage_certificate, name="manage_certificate"),
    path('<int:id>/delete_certificate', views.delete_certificate, name="delete_certificate"),
    path('<int:id>/download', views.generate_pdf, name="download"),
    path('verify_certificate', views.verify_certificate, name="verify_certificate"),
    path('<int:id>/verify', views.verify, name="verify"),
]