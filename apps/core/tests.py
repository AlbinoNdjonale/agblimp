from django.test import TestCase

from . import models

# Create your tests here.

class ServiceModelTest(TestCase):
    def test_create_service(self):
        service = models.Service(
            name = 'Service Test',
            price = 150,
            duration = 1
        )

        service.save()

        self.assertEqual(service.name, 'Service Test')
        self.assertEqual(service.price, 150)
        self.assertEqual(service.duration, 1)
        self.assertEqual(service.description, None)
        self.assertIn('id', service.__dict__.keys())

class ClientModelTest(TestCase):
    def test_create_client(self):
        client = models.Client(
            name    = 'client name',
            number  = '555555555',
            email   = 'example@gmail.com',
            address = 'endereço',
            cep     = '63.254-788'
        )

        client.save()

        self.assertEqual(client.name, 'client name')
        self.assertEqual(client.number, '555555555')
        self.assertEqual(client.email, 'example@gmail.com')
        self.assertEqual(client.address, 'endereço')
        self.assertEqual(client.cep, '63.254-788')
        self.assertIn('id', client.__dict__.keys())

class SchedulingModelTest(TestCase):
    def test_create_scheduling(self):
        service = models.Service(
            name = 'Service Test',
            price = 150,
            duration = 1
        )
        service.save()

        client = models.Client(
            name    = 'client name',
            number  = '555555555',
            email   = 'example@gmail.com',
            address = 'endereço',
            cep     = '63.254-788'
        )
        client.save()

        scheduling = models.Scheduling(
            service     = service,
            client      = client,
            date        = '2024-10-09 13:00',
            way_payment = 'a vista'
        )

        scheduling.save()

        self.assertEqual(scheduling.service, service)
        self.assertEqual(scheduling.client, client)
        self.assertEqual(scheduling.date, '2024-10-09 13:00')
        self.assertEqual(scheduling.way_payment, 'a vista')
        self.assertEqual(scheduling.status, 'pendente')
        self.assertIn('id', scheduling.__dict__.keys())

class TestimonyModelTest(TestCase):
    def test_create_testimony(self):        
        testimony = models.Testimony(
            name_client = 'nome do cliente',
            mesage      = 'uma mensagem'
        )

        testimony.save()

        self.assertEqual(testimony.name_client, 'nome do cliente')
        self.assertEqual(testimony.mesage, 'uma mensagem')
        self.assertEqual(testimony.status, 'pendente')

class FaqModelTest(TestCase):
    def test_create_faq(self):        
        faq = models.Faq(
            question = 'como',
            response = 'assim'
        )

        faq.save()

        self.assertEqual(faq.question, 'como')
        self.assertEqual(faq.response, 'assim')

class QuestionModelTest(TestCase):
    def test_create_question(self):        
        question = models.Question(
            name_client = 'nome do cliente',
            question = 'como'
        )

        question.save()

        self.assertEqual(question.name_client, 'nome do cliente')
        self.assertEqual(question.question, 'como')
