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

    @receiver(post_save, sender=SocialAccount)
    def social_login_profilepic(instance, **kwargs):
        preferred_profile_size_pixels = 256
        print("workng")
        request_user_id =instance.user_id
        user_intance = User.objects.get(id=request_user_id)
        if instance.provider == 'facebook':

            account_uid = SocialAccount.objects.filter(user_id=request_user_id, provider='facebook')
            UID = account_uid[0].extra_data['id']
            print(UID)
            print(request_user_id)
            picture_url = "http://graph.facebook.com/{0}/picture?width={1}&height={1}".format(
                        UID, preferred_profile_size_pixels)
            print(picture_url)
            create = Profile.objects.get(user_id=request_user_id)
            print(create)
            if not create or create:
                create.user = user_intance
                create.fb_pic_url = picture_url
                create.save()



