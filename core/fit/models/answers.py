from django.db import models
from django.conf import settings


class Answer(models.Model):
    
    survey = models.ForeignKey('Survey')
    question = models.ForeignKey('Question')
    value = models.IntegerField(default=1, help_text="Range: [1-6]")
