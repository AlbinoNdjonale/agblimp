from apps.core import forms
from apps.core import models
from django.core import serializers
from django.http import HttpRequest, HttpResponseRedirect, FileResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from urllib.parse import urlencode

# Create your views here.

def index(request: HttpRequest):
    services     = models.Service.objects.all()
    testimonies  = models.Testimony.objects.filter(status = 'aprovado')
    faqs         = models.Faq.objects.all()
    jobsopening  = models.JobOpening.objects.all()
    requires     = models.Requirements.objects.all()

    client = None
    clearcookkie = False
    if id := request.COOKIES.get('client'):
        clients = models.Client.objects.filter(id = id)
        if clients.exists():
            client = clients.first()
        else:
            clearcookkie = True

    
    response = render(request, 'web/index.html', {
        'services'   : services,
        'testimonies': testimonies,
        'faqs'       : faqs,
        'jobsopening': jobsopening,
        'requires'   : serializers.serialize('json', requires),
        'client'     : client,
        'msg'        : request.GET.get('msg'),
        'status'     : request.GET.get('status')
    })

    if clearcookkie:
        response.delete_cookie('client')

    return response


def scheduling(request: HttpRequest):
    client = None
    if request.method == 'POST':

        data_client = {
            key: request.POST.get(key)
            for key in [
                'name',
                'email',
                'address',
                'phone',
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
            if  (id := request.COOKIES.get('client')) and \
                    (clients := models.Client.objects.filter(id = id, name = data_client['name'], email = data_client['email'])).exists():
                        client = clients.first()
            else:
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
    
    response = HttpResponseRedirect(f'{reverse("web:index")}?{urlencode(query_params)}')
    
    if client and request.COOKIES.get('can_use_cookie'):
        response.set_cookie('client', client.id, max_age = 60*60*24*30)

    return response

def candidate(request: HttpRequest):
    form_candidate = forms.CreateCandidate(request.POST, request.FILES)
        
    try:
        assert form_candidate.is_valid()

        form_candidate.save()

        query_params = {
            'msg': 'Candidatura feita com sucesso',
            'status': 'ok'
        }
    except:
        query_params = {
            'msg': 'Não foi possivel registrar a sua candidatura',
            'status': 'err'
        }


    return HttpResponseRedirect(f'{reverse("web:index")}?{urlencode(query_params)}')