from django.urls import path
from HttpSessionApp import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('calci',views.Calci,name='calci'),
    path('display/',views.Display,name='display'),
]