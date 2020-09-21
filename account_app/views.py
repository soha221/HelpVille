from django.shortcuts import render,HttpResponseRedirect
from .forms import registerForm
from django.urls import reverse,reverse_lazy

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.http import  HttpResponse
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

                return HttpResponse("logged in")


    return render(request,'account_app/login.html',context={'form':form})
