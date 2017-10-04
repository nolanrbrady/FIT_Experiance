import uuid
from django.db import models
from django.conf import settings
from django.contrib import admin
from portal.core.fit.utils import ChoiceEnum


class DreamBuilder(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created = models.DateTimeField(auto_now_add=True)    
    modified = models.DateTimeField(auto_now=True)


class DreamEnviroment(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dreambuilder = models.ForeignKey('DreamBuilder')
    nutrient_people = models.TextField(blank=True)
    nutrient_places = models.TextField(blank=True)
    nutrient_resources = models.TextField(blank=True)
    toxic_people = models.TextField(blank=True)
    toxic_places = models.TextField(blank=True)
    toxic_resources = models.TextField(blank=True)


class Purpose(models.Model):
    
    text = models.TextField(blank=True)
    prompt = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.text[:24] + '...'


class PurposeAnswer(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    dreambuilder = models.ForeignKey('DreamBuilder')
    purpose = models.ForeignKey('Purpose')
    text = models.TextField(blank=True)
    active = models.BooleanField(default=True)


class PurposeStatement(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    dreambuilder = models.ForeignKey('DreamBuilder')
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Principle(models.Model):
    
    text = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class PrincipleAnswer(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dreambuilder = models.ForeignKey('DreamBuilder')
    principle = models.ForeignKey('Principle', null=True)
    text = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    @property
    def label(self):
        return self.principle.text


class CustomPrinciple(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class CustomPrincipleAnswer(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dreambuilder = models.ForeignKey('DreamBuilder')
    principle = models.ForeignKey('CustomPrinciple')
    text = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Vision(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dreambuilder = models.ForeignKey('DreamBuilder')
    title = models.TextField(blank=True)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    
