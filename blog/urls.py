from django.contrib import admin
from django.urls import path ,include

from . import views

urlpatterns = [
    
    path('',views.homePageView, name='home'),
    path('<slug:slug>,<int:id>/', views.my_view, name='article'),

]
