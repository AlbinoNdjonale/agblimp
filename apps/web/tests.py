from django.test import TestCase
from django.urls import reverse
from apps.core import models

# Create your tests here.

class SchedulingIntegrationTest(TestCase):
    @classmethod
    def setUpData(cls):

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
        
        self.assertTrue(models.Client.objects.filter(name = 'Nome do cliente').exists)
        # verifica se o cliente foi criado e salvo na base de dados