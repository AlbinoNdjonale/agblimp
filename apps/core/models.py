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
    addess      = models.CharField(max_length = 100)
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
        ('cancelado', 'Cancelado')
    ])
    way_payment = models.CharField(max_length = 50, choices = [
        ('cartão credito', 'Cartão credito'),
        ('Cartão debito', 'Cartão debito'),
        ('A vista', 'A vista')
    ])

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
    client      = models.ForeignKey(Client, on_delete = models.CASCADE, null = True)
    name_client = models.CharField(max_length = 50)
    mesage      = models.TextField()
    date        = models.DateField(auto_now_add = True)

    def __str__(self) -> str:
        return f'Depoimento de {self.name_client} em {self.date}'
    
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
