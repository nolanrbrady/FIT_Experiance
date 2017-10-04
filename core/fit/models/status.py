import uuid
from django.db import models
from django.conf import settings
from django.contrib import admin
from django.core.validators import RegexValidator
from portal.core.fit.utils import ChoiceEnum



class Status(models.Model):
    
    class Meta:
        verbose_name_plural = "statuses"
        get_latest_by = 'modified'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    dashboard = models.BooleanField(default=False)
    
    history = models.BooleanField(default=False)
    
    agenda = models.BooleanField(default=False)
    
    created = models.DateTimeField(auto_now_add=True)
    
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Status <{}>".format(self.user)
