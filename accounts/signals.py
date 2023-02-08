from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.models import Group

def profile(sender, instance, created,**kwargs):
     if created:
        group = Group.objects.get(name='users')
        instance.groups.add(group)
        
        Profile.objects.create(
            user=instance,
            name=instance.username,
        )

post_save.connect(profile, sender=User)

