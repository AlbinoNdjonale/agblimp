from django.db import models

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
    id          = models.UUIDField(unique = True, primary_key = True)
    name        = models.CharField(max_length = 50)
    email       = models.EmailField(max_length = 254)
    number      = models.CharField(max_length = 11)
    addess      = models.CharField(max_length = 100)
    cep         = models.CharField(max_length = 11)
    complemento = models.CharField(max_length = 20)

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
