from django.contrib import admin
from django.urls import path ,include
from .views import views

urlpatterns = [
    
    path('',homePageView, name='home'),
    path('posts/<slug:the_slug>/', views.post_detail, name='show_post'),
]
