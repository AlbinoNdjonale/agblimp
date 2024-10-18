from django.contrib import admin
from . import models

admin.site.register(models.Service)
admin.site.register(models.Client)
admin.site.register(models.Scheduling)
admin.site.register(models.Testimony)
admin.site.register(models.Faq)
admin.site.register(models.Question)
admin.site.register(models.JobOpening)
admin.site.register(models.Requirements)
admin.site.register(models.Candidate)
