from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others Specify', 'Others Specify')
    )

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null = True)
    about = models.TextField(null=True)
    date_of_birth = models.DateField(null = True)
    gender = models.CharField(max_length=50, null = True, choices = GENDER_CHOICES)
    linkedin_id = models.CharField(max_length=255, null=True, blank = True)
    facebook_handle = models.CharField(max_length=255, null=True, blank = True)
    twitter_handle = models.CharField(max_length=255, null=True, blank = True)
    instagram_handle = models.CharField(max_length=255, null=True, blank = True)
    website = models.CharField(max_length=255, null=True, blank = True)
    country = models.CharField(max_length=255, null=True, blank = True)
    state = models.CharField(max_length=255, null=True, blank = True)
    profile_pic = models.ImageField(null=True, blank = True, upload_to = "profile/")

    def __str__(self):
        return self.name
    
