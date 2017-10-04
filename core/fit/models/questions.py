from django.db import models
from django.contrib import admin
from portal.core.fit.utils import ChoiceEnum


class QuestionStyle(ChoiceEnum):
    Normal = 0
    NoneToALot = 1
    LessWorriedMuchHappier = 2
    Creditors = 3
    Mortgage = 4
    Success = 5
    NA = 6
    Television = 7


class Question(models.Model):
    
    seq = models.IntegerField(default=0, help_text="Sequence Order")
    content = models.TextField()
    is_reversed = models.BooleanField(default=False, help_text="answer.Value = -(answer.Value - 6)")
    is_active = models.NullBooleanField(default=True, null=True)
    is_corp = models.BooleanField(default=False)
    dimension = models.ForeignKey('Dimension', null=True)
    subcategory = models.ForeignKey('SubCategory', null=True)
    weight = models.IntegerField(default=1)
    style = models.IntegerField(choices=QuestionStyle.choices(), default=0) # was QuestionTypeId
    
    def __str__(self):
        return '%s - %03d: %s' % (self.dimension, self.id, self.content)

