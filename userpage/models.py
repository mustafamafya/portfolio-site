from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# ✅ Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(max_length= 20 ,blank=True, null=True)
    profile_picture = models.ImageField(default='images/profilepic.png', upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return str(self.user)
