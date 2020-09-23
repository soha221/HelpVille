from django.db import models
from django.contrib.auth.models import User

# class UserProfile(models.Model):
#     user = models.OneToOneField(User,on_delete = models.CASCADE)
#     first_name = models.CharField(max_length = 256, blank=True)
#     last_name  = models.CharField(max_length = 256, blank=True)
#     gender = models.CharField(max_length= 256,blank=True)
#     profile_pic = models.ImageField(upload_to = 'profile_pictures',blank=True)
#     phn_number = models.IntegerField(blank=True)
#     facebook = models.URLField(blank=True)
#
#     def __str__(self):
#         return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=264, blank=True)
    full_name = models.CharField(max_length=264, blank=True)
    address_1 = models.TextField(max_length=300, blank=True)
    city = models.CharField(max_length=40, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username + "'s Profile"

    def is_fully_filled(self):
        fields_names = [f.name for f in self._meta.get_fields()]

        for field_name in fields_names:
            value = getattr(self, field_name)
            if value is None or value=='':
                return False
        return True
