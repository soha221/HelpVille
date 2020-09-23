from django.shortcuts import render,HttpResponseRedirect
from account_app.forms import registerForm, ProfileForm
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.http import  HttpResponse
from account_app.models import  Profile
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    form = registerForm()

    if request.method == "POST":
        form = registerForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("account_app:login"))


    return render(request,'account_app/signup.html',context={'form':form})


def signIn(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)

                return HttpResponseRedirect(reverse('Home:home'))


    return render(request,'account_app/login.html',context={'form':form})

@login_required
def logOut(request):
    logout(request)
    # messages.warning(request, "You are logged out!!")
    return HttpResponseRedirect(reverse('Home:home'))

@login_required
def profile(request):
    return render(request,'account_app/profile.html')

@login_required
def user_profile(request):
    profile = request.user
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            # messages.success(request, "Change Saved!!")
            form = ProfileForm(instance=profile)
    return render(request, 'account_app/edit_profile.html', context={'form':form})
