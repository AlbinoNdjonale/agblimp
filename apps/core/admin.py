from django.contrib import admin
from . import models

admin.site.register(models.Service)
admin.site.register(models.Client)
admin.site.register(models.Scheduling)
admin.site.register(models.Testimony)
admin.site.register(models.Faq)
admin.site.register(models.JobOpening)
admin.site.register(models.Requirements)
admin.site.register(models.Candidate)
admin.site.register(models.GeneralInformation)
admin.site.register(models.ServiceLocation)
admin.site.register(models.CompletedSerive)
admin.site.register(models.CanceledAppointment)
admin.site.register(models.Collaborator)
admin.site.register(models.PaymentHistory)
admin.site.register(models.Transport)