from  django.urls import  path
from Home import views

app_name = "Home"

urlpatterns =[
    path('home/',views.home,name='home'),
    path('reviews/',views.reviews,name='reviews'),
    path('categories/',views.category,name='categories'),
    path('booth/',views.booth,name='booth')
    ]
