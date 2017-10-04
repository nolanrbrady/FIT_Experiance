import uuid
from django.db import models
from django.conf import settings
from django.contrib import admin
from django.core.validators import URLValidator
from django.core.urlresolvers import reverse_lazy


class Resource(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subcategory = models.ForeignKey('SubCategory')
    url = models.TextField(validators=[URLValidator()], blank=True)
    embed = models.TextField(blank=True,
        help_text= 'Full iframe embed code from YouTube or Vimeo.'
    )
    upload = models.FileField(upload_to='lib/%Y/%m/%d/', blank=True)
    thumbnail = models.FileField(upload_to='lib/%Y/%m/%d/thumbnail', blank=True)
    title = models.TextField()
    description = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('fit:library_resource', kwargs={'resource_id':self.id})
        
    @property
    def ID(self):
        return str(self.id)
    
    @property
    def dimension(self):
        return self.subcategory.dimension
