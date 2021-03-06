"""mblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include

from mainsite.views import homepage, showpost
from newtable.views import about, listing, disp_detail

urlpatterns = [
    path('admin/', admin.site.urls,name="index"),
    path('',homepage),
    re_path('post/(\w+)/', showpost),
    # path('favicon.ico', serve, {'path': 'images/favicon.ico'}),
    path('about/',about,name='about'),
    re_path('list/([0-9]+)/',disp_detail),
    path('list/',listing,name='listing'),
    path('video/', include('video.urls'), name='video_index'),
    path('ch08www/', include('ch08www.urls'), name='ch08ww_index'),


]
