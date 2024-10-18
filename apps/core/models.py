from django.contrib.auth.models import User
from django.db import models
import uuid

class Service(models.Model):
    '''
      Modelo serviço
    '''
    name        = models.CharField(max_length = 50)
    description = models.TextField(null = True)
    price       = models.FloatField()
    duration    = models.IntegerField()
    image       = models.FileField(upload_to = 'media/service/', max_length = 100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name        = 'Service'
        verbose_name_plural = 'Services'

class Client(models.Model):
    '''
      Modelo Cliente, não sera feito directamente
    o registro de clientes mas durante o agendamento
    o cliente devera fornecer seus dados
    '''
    id          = models.UUIDField(primary_key = True, editable = False, default = uuid.uuid4)
    name        = models.CharField(max_length = 50)
    email       = models.EmailField(max_length = 254)
    number      = models.CharField(max_length = 11)
    address      = models.CharField(max_length = 100)
    cep         = models.CharField(max_length = 11)
    complemento = models.CharField(max_length = 20, null = True, blank = True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name        = 'Client'
        verbose_name_plural = 'Clients'

class Scheduling(models.Model):
    '''
      Modelo agendamento
    '''
    service = models.ForeignKey(Service, on_delete = models.CASCADE)
    client  = models.ForeignKey(Client, on_delete = models.CASCADE)
    date    = models.DateTimeField()
    status  = models.CharField(max_length = 12, choices = [
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
        ('pendente', 'Pendente')
    ], default = 'pendente')
    way_payment = models.CharField(max_length = 50, choices = [
        ('cartão credito', 'Cartão credito'),
        ('cartão debito', 'Cartão debito'),
        ('a vista', 'A vista')
    ])
    collaborator = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = True)

    def __str__(self) -> str:
        return f'Agedamento de {self.client.name} em {self.date}'
    
    class Meta:
        verbose_name        = 'Scheduling'
        verbose_name_plural = 'Schedulings'

class Testimony(models.Model):
    '''
      Modelo depoimento, ele tem os atributos
    name_client e client, onde o client pode ser
    nulo onde o name_client só será necessário
    se o client for nulo
    '''
    client      = models.ForeignKey(Client, on_delete = models.CASCADE, null = True, blank = True)
    name_client = models.CharField(max_length = 50)
    mesage      = models.TextField()
    score       = models.IntegerField()
    status      = models.CharField(max_length = 12, choices = [
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado'),
        ('pendente', 'Pendente')
    ], default = 'pendente')

    def __str__(self) -> str:
        return f'Depoimento de {self.name_client}'
    
    class Meta:
        verbose_name        = 'Testimony'
        verbose_name_plural = 'Testimonies'

class Faq(models.Model):
    '''
      Modelo Faq ou perguntas frequentes
    usado para registrar as perguntas frequentes
    e os suas respectivas respostas
    '''
    question = models.TextField()
    response = models.TextField()

    def __str__(self) -> str:
        if len(self.question) <= 50:
            return self.question
        
        return self.question[:50]+'...'
    
    class Meta:
        verbose_name        = 'Faq'
        verbose_name_plural = 'Faqs'

class Question(models.Model):
    '''
      Lembra do modelo Faq,
    pois este é modelo das perguntas
    feitas pelos os usuários
    '''
    client      = models.ForeignKey(Client, on_delete = models.CASCADE, null = True, blank = True)
    name_client = models.CharField(max_length = 50)
    question    = models.TextField()
    date        = models.DateField(auto_now_add = True)

    def __str__(self) -> str:
        if len(self.question) <= 50:
            return self.question
        
        return self.question[:50]+'...'
    
    class Meta:
        verbose_name        = 'Question'
        verbose_name_plural = 'Questions'

class JobOpening(models.Model):
    title             = models.CharField(max_length = 50)
    description       = models.TextField()
    short_description = models.TextField(max_length = 50)
    salary            = models.FloatField(null = True)

    def __str__(self) -> str:
        return self.title

class Requirements(models.Model):
    title      = models.CharField(max_length = 50)
    required   = models.BooleanField(default = True)
    jobopening = models.ForeignKey(JobOpening, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f'requisito {self.title} para a vaga de {self.jobopening}'

class Candidate(models.Model):
    name             = models.CharField(max_length = 130)
    email            = models.EmailField(max_length = 254)
    job              = models.ForeignKey(JobOpening, on_delete = models.CASCADE)
    curriculum_vitae = models.FileField(upload_to = 'media/curriculum_vitae/', max_length = 100, null = True, blank = True)
    mesage           = models.TextField(null = True, blank = True)

    def __str__(self) -> str:
        return f'candidato {self.name} para a vaga de {self.job}'