from django.contrib import admin
from .models import UserProfile,UserDonation
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserDonation)
