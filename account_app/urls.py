from  django.urls import  path
from account_app import views

app_name = "account_app"

urlpatterns =[
    path('signup/',views.register,name='signup'),
    path('login/',views.signIn,name='login'),
    path('logout/', views.logOut, name='logout'),
    path('profile/',views.profile,name='profile'),
    path('editProfile/',views.user_profile,name='editProfile'),
    path('donation/',views.donation_page,name='donation'),
    path('createUser/',views.CreateProfilePage.as_view(),name='createProfile'),


]
