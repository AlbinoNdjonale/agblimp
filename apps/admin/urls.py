from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = 'admin'

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),

    path('auth/login', LoginView.as_view(template_name = 'admin1/login.html'), name = 'login')
]
