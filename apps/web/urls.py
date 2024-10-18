from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('scheduling', views.scheduling, name = 'scheduling'),
    path('candidate', views.candidate, name = 'candidate')
]
