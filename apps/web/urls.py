from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('scheduling', views.scheduling, name = 'scheduling'),
    path('testimony', views.testimony, name = 'testimony')
]
