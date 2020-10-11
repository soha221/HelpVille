from django.db import models
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import User

# To automatically create one to one objects

from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,related_name='user_profile')
    full_name = models.CharField(max_length=256,blank=True)
    gender = models.CharField(max_length= 256,blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pictures',blank=True)
    phn_number = models.CharField(max_length=20,blank=True)
    facebook = models.URLField(blank=True)
    address = models.TextField(max_length=400,blank=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save,sender=User)
def create_profile(sender, instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender,instance,**kwargs):
    instance.user_profile.save()




class UserDonation(models.Model):
    donar = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='user_d')
    category = models.CharField(max_length=256,blank=True)
    item_name = models.CharField(max_length=256,blank=True)
    num_of_item = models.IntegerField(blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.donar)

    class Meta:
        ordering = ["-upload_date",]
