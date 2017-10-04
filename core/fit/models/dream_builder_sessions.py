from django.db import models
from django.conf import settings


class DreamBuilderSession(models.Model):

    sequence_state = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
