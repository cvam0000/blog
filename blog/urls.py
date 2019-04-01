from django.contrib import admin
from django.urls import path ,include

from . import views

urlpatterns = [
    
    path('',views.homePageView, name='home'),
    #path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('article/embeddedsystems/cvam/<int:pk>/', views.post_detail, name='article'),

]
