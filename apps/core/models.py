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