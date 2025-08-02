from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User
# ✅ Signal to create profile when user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# ✅ Signal to save profile when user is updated
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, **kwargs):
    instance.profile.save()