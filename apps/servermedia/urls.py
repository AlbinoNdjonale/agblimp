from django.urls import re_path
from . import views

app_name = 'servermedia'

urlpatterns = [
    re_path(r'^(?P<file_path>.+)/$', views.media, name = 'servermedia')
]
