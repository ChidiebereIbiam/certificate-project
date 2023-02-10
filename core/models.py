from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate_number = models.CharField(unique=True, max_length=50)
    role = models.CharField(max_length=225)
    organization = models.CharField(default="Kartexa", max_length=255)
    internship_organizer = models.CharField(max_length=225)
    internship_name = models.CharField(max_length=250)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    generated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.certificate_number}"
    

