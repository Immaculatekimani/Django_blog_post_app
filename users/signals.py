from django.db.models.signals import post_save  #the signal that is fired whenever an object is saved
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#when sender posts save then the signal is received by the receiver and the receiver then creates a profile
#the receiver is a decorator the function receives arguments passed to it by the post save period
@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
  #the instance is going to be the user remember
      