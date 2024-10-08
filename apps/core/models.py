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