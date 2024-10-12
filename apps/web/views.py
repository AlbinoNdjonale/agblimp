from apps.core import forms
from apps.core import models
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def index(request: HttpRequest):
    services = models.Service.objects.all()

    print(request.GET)

    return render(request, 'web/index.html', {
        'services': services,
        'msg': request.GET.get('msg'),
        'status': request.GET.get('status')
    })

def scheduling(request: HttpRequest):
    if request.method == 'POST':

        data_client = {
            key: request.POST.get(key)
            for key in [
                'name',
                'email',
                'address',
                'number',
                'cep',
                'complemento'
            ]
        }

        data_scheduling = {
            key: request.POST.get(key)
            for key in [
                'way_payment',
                'service',
                'date'
            ]
        }

        form_client     = forms.CreateClient(data_client)
        form_scheduling = forms.CreateScheduling(data_scheduling)

        if form_client.is_valid() and form_scheduling.is_valid():
            client = models.Client(**data_client)
            client.save()
            
            data_scheduling['service'] = models.Service.objects.get(id = data_scheduling['service'])
            
            scheduling = models.Scheduling(client = client, **data_scheduling)
            scheduling.save()

    return HttpResponseRedirect(reverse('web:index'))