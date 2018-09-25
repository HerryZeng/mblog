from django.urls import path, re_path

from ch08www.views import index

app_name = 'ch08www'

urlpatterns = [
    path('', index, name='index'),
    re_path('(\d{1})/', index, name='tv-url'),
]
