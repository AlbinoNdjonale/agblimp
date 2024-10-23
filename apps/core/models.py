from django.contrib.auth.models import User
from django.db import models
import uuid

class Collaborator(models.Model):
    user        = models.OneToOneField(User, on_delete = models.CASCADE)
    number      = models.CharField(max_length = 15)
    rg          = models.CharField(max_length = 20, null = True, blank = True, unique = True)
    cpf         = models.CharField(max_length = 14, null = True, blank = True)
    address     = models.CharField(max_length = 255)
    cep         = models.CharField(max_length = 10)
    rua         = models.CharField(max_length = 255)
    complemento = models.CharField(max_length = 100, null = True, blank = True)
    cargo       = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return f'Colaborador {self.user.username}'

class Transport(models.Model):
    motorista = models.CharField(max_length = 255)
    time      = models.TimeField()
    type = models.CharField(max_length = 7, choices = [
        ('carro', 'Carro'),
        ('ônibus', 'Ônibus'),
        ('moto', 'Moto')
    ])
    value    = models.DecimalField(max_digits = 10, decimal_places = 2)
    paid_for = models.CharField(max_length = 50, choices = [
        ('empresa', 'Empresa'),
        ('colaborador', 'Colaborador'),
        ('cliente', 'Cliente'),
    ])

    def __str__(self):
        return f'Transporte {self.id}'

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
    phone       = models.CharField(max_length = 15)
    number      = models.CharField(max_length = 10, null = True, blank = True)
    address     = models.CharField(max_length = 100)
    cep         = models.CharField(max_length = 11)
    complemento = models.CharField(max_length = 20, null = True, blank = True)
    road        = models.CharField(max_length = 255, null = True, blank = True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name        = 'Client'
        verbose_name_plural = 'Clients'

class Scheduling(models.Model):
    '''
      Modelo agendamento
    '''
    service           = models.ForeignKey(Service, on_delete = models.CASCADE)
    client            = models.ForeignKey(Client, on_delete = models.CASCADE)
    date              = models.DateTimeField()
    registration_date = models.DateTimeField(auto_now_add = True)
    status  = models.CharField(max_length = 12, choices = [
        ('em andamento', 'Em andamento'),
        ('reprovado', 'Reprovado'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
        ('pendente', 'Pendente')
    ], default = 'pendente')
    way_payment = models.CharField(max_length = 50, choices = [
        ('cartão credito', 'Cartão credito'),
        ('cartão debito', 'Cartão debito'),
        ('a vista', 'A vista')
    ])
    collaborator       = models.ForeignKey(Collaborator, on_delete = models.DO_NOTHING, null = True)
    outbound_transport = models.ForeignKey(Transport, on_delete = models.DO_NOTHING, null = True, related_name = 'outbound_transport')
    return_transport   = models.ForeignKey(Transport, on_delete = models.DO_NOTHING, null = True, related_name = 'return_transport')
    hour_spent         = models.DecimalField(max_digits = 5, decimal_places = 2, null = True)

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
    client      = models.ForeignKey(Client, on_delete = models.DO_NOTHING, null = True, blank = True)
    name_client = models.CharField(max_length = 50)
    mesage      = models.TextField()
    score       = models.DecimalField(max_digits = 2, decimal_places = 1)
    capa        = models.FileField(upload_to = 'media/testimony/', max_length = 100)
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

class PaymentHistory(models.Model):
    scheduling = models.ForeignKey(Scheduling, on_delete = models.CASCADE)
    status     = models.CharField(max_length = 50, choices = [
        ('pago', 'Pago'),
        ('não pago', 'Não pago')
    ])
    payment_date =  models.DateField()

    def __str__(self):
        return f'Historico de pagamento do {self.scheduling}'

class CompletedSerive(models.Model):
    scheduling           = models.ForeignKey(Scheduling, on_delete = models.CASCADE)
    completed_date       = models.DateField()
    customer_satisfation = models.CharField(max_length = 50, choices = [
        ('satisfeito', 'Satisfeito'),
        ('muito satisfeito', 'Muito satisfeito'),
        ('insatisfeito', 'insatisfeito'),
        ('muito insatisfeito', 'Muito insatisfeito')
    ])

    def __str__(self):
        return f'{self.scheduling} completado'

class CanceledAppointment(models.Model):
    scheduling = models.ForeignKey(Scheduling, on_delete = models.CASCADE)
    reason     = models.TextField()
    date       = models.DateField(auto_now_add = True)

    def __str__(self):
        return f'{self.scheduling} cancelado'

class ServiceLocation(models.Model):
    name         = models.CharField(max_length = 255)
    min_cep      = models.CharField(max_length = 10)
    max_cep      = models.CharField(max_length = 10)
    city         = models.CharField(max_length = 100)
    estate       = models.CharField(max_length = 50)
    active       = models.BooleanField()
    date         = models.DateField(auto_now_add = True)
    collaborator = models.ForeignKey(Collaborator, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return f'Local de atendimento {self.name}'

class GeneralInformation(models.Model):
    n_service_day = models.IntegerField(null = True)
    email         = models.EmailField(max_length = 254, null = True, blank = True)
    whatsapp      = models.CharField(max_length = 15, null = True, blank = True)
    phone         = models.CharField(max_length = 15, null = True, blank = True)
    facebook      = models.CharField(max_length = 150, null = True, blank = True)
    instagram     = models.CharField(max_length = 150, null = True, blank = True)
    aboutus       = models.TextField(null = True, blank = True)
    mission       = models.TextField(null = True, blank = True)
    vision        = models.TextField(null = True, blank = True)
    yearexpirence = models.IntegerField(null = True)
    clients       = models.IntegerField(null = True)
    professional  = models.IntegerField(null = True)
    projects      = models.IntegerField(null = True)

    def __str__(self):
        return 'Informações gerais'