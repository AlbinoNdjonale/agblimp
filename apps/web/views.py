from apps.core import forms
from apps.core import models
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from urllib.parse import urlencode

# Create your views here.

def index(request: HttpRequest):
    services    = models.Service.objects.all()
    testimonies = models.Testimony.objects.filter(status = 'aprovado')

    return render(request, 'web/index.html', {
        'services': services,
        'testimonies': testimonies,
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

            query_params = {
                'msg': 'Serviço agendado com sucesso, por favor aguarde pela nossa resposta',
                'status': 'ok'
            }
        else:
            query_params = {
                'msg': 'Não foi possivel agendar o serviço, tente de novo',
                'status': 'error'
            }

    return HttpResponseRedirect(f'{reverse("web:index")}?{urlencode(query_params)}')

def testimony(request: HttpRequest):
    form = forms.CreateTestimony(request.POST)

    if form.is_valid():
        testimony = models.Testimony(
            status = 'pendente',
            mesage = request.POST['mesage'],
            name_client = request.POST['name_client']
        )
        testimony.save()

        query_params = {
            'msg': 'Agradecemos pelo seu depoimento',
            'status': 'ok'
        }
    else:
        query_params = {
            'msg': 'Não foi possivel guardar o seu depoimento, tente de novo',
            'status': 'erro'
        }

    return HttpResponseRedirect(f'{reverse("web:index")}?{urlencode(query_params)}')