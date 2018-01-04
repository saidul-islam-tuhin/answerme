from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photo/', blank=True)
    fb_pic_url = models.CharField(max_length=256, blank=True, null=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        print("this working")
        if created:
            print("created working")
            Profile.objects.create(user=instance)
        instance.profile.save()
