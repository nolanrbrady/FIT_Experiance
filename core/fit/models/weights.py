from django.db import models
from django.conf import settings


public class WeightScore(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    survey = models.ForeignKey('Survey')
    dimension = models.ForeignKey('Dimension') # ?
    weight = models.DecimalField(default=1) 
    name = models.TextField(blank=True)
    color = models.CharField(max_length=7, default='#DDDDDD')
    score = models.DecimalField(default=0)
