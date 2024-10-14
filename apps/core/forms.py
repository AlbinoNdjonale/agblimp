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

class CreateTestimony(ModelForm):
    class Meta:
        model = models.Testimony

        fields = [
            'name_client',
            'mesage'
        ]