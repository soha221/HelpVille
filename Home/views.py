from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect

# Create your views here.


def home(request):
    return render(request,'Home/home.html')



def reviews(request):
    return render(request,'Home/reviews.html')


def category(request):
    return render(request,'Home/category.html')


def booth(request):
    return render(request,'Home/booth.html')
