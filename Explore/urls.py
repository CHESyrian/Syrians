"""Syrians URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', Explore_Page, name='Explore'),
    path('news/', News_Page, name='News'),
    path('news/posts/', News_Posts, name='News_Posts'),
    path('news/images/', News_Images, name='News_Images'),
    path('serach/', Search, name='Search'),
    path('search/users/<str:keyword>/', Search_Users, name='Search_Users'),
    path('search/posts/<str:keyword>/', Search_Posts, name='Search_Posts'),
    path('search/images/<str:keyword>/', Search_Images, name='Search_Images'),
]\
    +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
