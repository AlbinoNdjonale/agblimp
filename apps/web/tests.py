from django.db import connection
from django.test import TestCase
from django.urls import reverse
from apps.core import models

# Create your tests here.

def reset_id_sequence(model):
    with connection.cursor() as cursor:
        cursor.execute(f"ALTER SEQUENCE {model._meta.db_table}_id_seq RESTART WITH 1;")

class SchedulingIntegrationTest(TestCase):
    def setUp(self):
        reset_id_sequence(models.Service)
        # cria um serviço para poder ser usado nos testes
        models.Service(
            name        = 'nome do serviço',
            price       = 150,
            duration    = 1,
            description = 'descrição do serviço'
        ).save()

    def test_create_sheduling(self):
        response = self.client.post(reverse('web:scheduling'), {
            'name'       : 'Nome do cliente',
            'email'      : 'example@gmail.com',
            'address'    : 'endereço do cliente',
            'number'     : '555555555',
            'cep'        : '63.254-788',
            # este endpoint cria um cliente na
            # base de dados a partir dos dados do formulario de agendamento
            'way_payment': 'a vista',
            'service'    : '1',
            'date'       : '2024-11-17 12:00'
        })

        self.assertEqual(response.status_code, 302)
        # verificar se o endpoint esta retornando uma resposta de redirecionamento
        
        self.assertTrue(models.Client.objects.filter(name = 'Nome do cliente').exists())
        # verifica se o cliente foi criado e salvo na base de dados

class CandidateIntegrationTest(TestCase):
    def setUp(self):
        reset_id_sequence(models.JobOpening)
        # cria uma vaga para poder ser usado nos testes
        models.JobOpening(
            title             = 'titulo da vaga',
            description       = 'descrição da vaga',
            short_description = 'breve descrição',
            salary            = 1800
        ).save()

    def test_create_candidate(self):
        response = self.client.post(reverse('web:candidate'), {
            'name'  : 'Nome do candidato',
            'email' : 'example@gmail.com',
            'job'   : '1',
            'mesage': 'uma mensagem para os recrutadores'
        })

        self.assertEqual(response.status_code, 302)
        # verificar se o endpoint esta retornando uma resposta de redirecionamento

        self.assertTrue(models.Candidate.objects.filter(name = 'Nome do candidato').exists())
        # verifica se o candidato foi criado e salvo na base de dados