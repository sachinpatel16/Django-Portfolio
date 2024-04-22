import django
from django.contrib import admin
from django.urls import path
from servies import views


urlpatterns = [
    path('',views.index,name='index'),
    path('pa/',views.pa,name='pa'),
    path('pd/<int:pk>/',views.pd,name='pd'),
    path('del/<int:pk>/',views.delete,name='del'),
]
