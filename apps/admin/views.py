from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

@login_required
def dashboard(request: HttpRequest):
    return render(request, 'admin1/dashboard.html')
