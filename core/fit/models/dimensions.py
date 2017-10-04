from django.db import models
from django.contrib import admin
from portal.core.fit.utils import ChoiceEnum


class DimensionId(ChoiceEnum):
    Cognitive = 1
    Emotional = 2
    Physical = 3
    Financial = 4


class Dimension(models.Model):

    id = models.IntegerField(primary_key=True, choices=DimensionId.choices())    
    name = models.TextField()
    divisor = models.IntegerField(default=5)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return "%i: %s" % (self.id, self.name)


class SubCategory(models.Model):
    
    name = models.TextField()
    dimension = models.ForeignKey('Dimension')
    multiplier = models.IntegerField(default=5)
    
    def __str__(self):
        return "%02d: %s" % (self.id, self.name)


admin.site.register(Dimension)
admin.site.register(SubCategory)
