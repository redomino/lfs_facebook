from django.db import models
from django.contrib.auth.models import User
from django_facebook.models import FacebookProfileModel

class LfsFbUser(FacebookProfileModel):
    user = models.OneToOneField(User)
    fb_like_flag = models.BooleanField(default=False)

    class Meta():
            db_table = 'fb_data'


from django.db.models.signals import post_save

#Make sure we create a MyCustomProfile when creating a User
def create_facebook_profile(sender, instance, created, **kwargs):
    if created:
        LfsFbUser.objects.create(user=instance)

post_save.connect(create_facebook_profile, sender=User)

