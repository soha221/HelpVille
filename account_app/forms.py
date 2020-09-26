from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from account_app.models import UserProfile,UserDonation



class registerForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields =('username','email','password1','password2')


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

class CreateProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields =('full_name','gender','profile_pic','phn_number','facebook','address')



class DonationForm(ModelForm):
    class Meta:
        model = UserDonation
        exclude =('donar',)
