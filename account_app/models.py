from django.db import models
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,related_name='user_profile')
    full_name = models.CharField(max_length=256,blank=True)
    gender = models.CharField(max_length= 256,blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pictures',blank=True)
    phn_number = models.IntegerField(blank=True)
    facebook = models.URLField(blank=True)
    address = models.TextField(max_length=400,blank=True)

    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):
        return reverse('Home:home')

class UserDonation(models.Model):
    donar = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='user_d')
    category = models.CharField(max_length=256,blank=True)
    item_name = models.CharField(max_length=256,blank=True)
    num_of_item = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.donar)
