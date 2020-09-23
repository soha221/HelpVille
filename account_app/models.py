from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,related_name='user_profile')
    first_name = models.CharField(max_length = 256, blank=True)
    last_name  = models.CharField(max_length = 256, blank=True)
    gender = models.CharField(max_length= 256,blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pictures',blank=True)
    phn_number = models.IntegerField(blank=True)
    facebook = models.URLField(blank=True)
