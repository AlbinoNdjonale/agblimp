from django.forms import ModelForm

from . import models

class CreateScheduling(ModelForm):
    class Meta:
        model = models.Scheduling

        fields = [
            'service',
            'date',
            'way_payment'
        ]

class CreateClient(ModelForm):
    class Meta:
        model = models.Client

        fields = '__all__'