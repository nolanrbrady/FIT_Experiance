import logging
import six
import uuid
import datetime as dt
import dateutil.parser
from django.db import models
from django.conf import settings
from django.contrib import admin
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from portal.core.fit.utils import ChoiceEnum

logger = logging.getLogger('fit')

class Goal(models.Model):
    
    subcategory = models.ForeignKey('SubCategory')
    text = models.TextField()

    def __str__(self):
        return '{}: {}'.format(self.id, self.text)


class Task(models.Model):
    
    goal = models.ForeignKey('Goal')
    text = models.TextField()

    def __str__(self):
        max_len = 40
        category = self.goal.subcategory.name
        ellipsis = '...' if len(self.text) > max_len else ''
        return "{}: {} / {}{}".format(self.id, category, self.text[:max_len], ellipsis)


class Agenda(models.Model):
    
    class Meta:
        get_latest_by = 'created'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    open = models.BooleanField(default=True)
    
    active = models.BooleanField(default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{}: {}".format(self.user, self.open)


# planbuilder.PlanBuilderObject
#
class Objective(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
        
    subcategory = models.ForeignKey('SubCategory')
    
    agenda = models.ForeignKey('Agenda')
    
    goal = models.ForeignKey('Goal')
    
    created = models.DateTimeField(auto_now_add=True)
    
    modified = models.DateTimeField(auto_now=True)
    
    #schedule = models.CharField(blank=True, max_length=60)
    
    # name
    label = models.CharField(
        max_length=60,
        blank=True,
        validators=[
            RegexValidator(regex='([\w\.-]+)',
                message='Invalid Chronos name.',
            ),
        ])
    
    def __str__(self):
        return "{}: {}".format(self.user, self.id)


class Plan(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    objective = models.ForeignKey('Objective')
    
    task = models.ForeignKey('Task')
    
    start = models.DateTimeField(null=True)
    
    end = models.DateTimeField(null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    
    modified = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # TODO: apply event heuristics
        try:
            if isinstance(self.start, six.string_types):
                start = dateutil.parser.parse(self.start)
            else:
                start = self.start
            if isinstance(self.end, six.string_types):
                end = dateutil.parser.parse(self.end)
            else:
                end = self.end  
            min_delta = dt.timedelta(hours=1)
            if (end - start) < min_delta:
                self.end = start + min_delta
        except Exception as e:
            logger.error("ERROR: <PlanId>{}".format(self.id)) 
        super(self.__class__, self).save(*args, **kwargs)
    
    @property
    def text(self):
        return self.objective.goal.text
    
    @property
    def user(self):
        return self.objective.user
    
    @property
    def goal(self):
        return self.objective.goal
    
    @property
    def dimension(self):
        return self.objective.subcategory.dimension
        
    @property
    def subcategory(self):
        return self.objective.subcategory
        
    @property
    def description(self):
        return self.task.text
    
    def __str__(self):
        return "{}: {}".format(self.user.email, self.id)


class Progress(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    plan = models.ForeignKey('Plan')
    delta = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)


admin.site.register(Goal)
admin.site.register(Task)
