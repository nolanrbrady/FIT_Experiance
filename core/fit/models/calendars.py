from django.db import models
from django.conf import settings


class Calendar(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    start_date = models.DateField()
    end_date = models.DateField()


class Goal(models.Model):
    
    content = models.TextField()
    subcategory = models.ForeignKey('SubCategory') 


class Task(models.Model):
    
    content = models.TextField()
    goal = models.ForeignKey('Goal')


class Plan(models.Model):
    
    content = TextField(blank=True)
    schedule = models.TextField(help_text='ISO 8601 repeating interval notation')
