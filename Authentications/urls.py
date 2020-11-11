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
    path('login/'                            , Login_Page       , name='Login_Page'),
    path('logging/'                          , Logging_In       , name='Logging'),
    path('register/'                         , Register_Page    , name='Register_Page'),
    path('username_validate/<str:user_name>/', Username_Validate, name='Username_Validate'),
]\
    +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
