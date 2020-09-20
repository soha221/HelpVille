from  django.urls import  path
from account_app import views

app_name = "account_app"

urlpatterns =[
    path('signup/',views.register,name='signup'),
    path('login/',views.signIn,name='login'),
]
