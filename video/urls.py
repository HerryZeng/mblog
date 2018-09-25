from django.urls import path, re_path

from video.views import index

app_name = 'video'

urlpatterns = [
    path('', index, name='index'),
    re_path('(\d{1})/', index, name='tv-url'),
]
