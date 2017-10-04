import os
from collections import namedtuple, defaultdict
from django.utils.safestring import mark_safe
from django.contrib.auth.mixins import LoginRequiredMixin

import portal.core.fit.models as models

from . import base

templates = os.path.join(base.APP_PATH, 'library')

Coach = namedtuple('Coach',('name','bioId', 'hexId'))

COACHES = {
    'PHYSICAL': Coach('Shane Niemeyer', 'Shane_Niemeyer', 'Shane'),
    'COGNITIVE': Coach('Rena Kirkland', 'Rena_Kirkland', 'Rena'),
    'EMOTIONAL': Coach('Ilene Rusk', 'Ilene_Rusk', 'Ilene'),
    'FINANCIAL': Coach('James Doran', 'James_Doran', 'James'),
} 

class LibraryDimensionView(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(templates, 'dimension.html')
    
    def get_context_data(self, dimension_id, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        dimension = models.Dimension.objects.get(pk=dimension_id)
        resources = models.Resource.objects.filter(subcategory__dimension=dimension)
        sections = defaultdict(list)
        for resource in resources:
            sections[resource.subcategory].append(resource)
        context.update({
            'coach': COACHES[dimension.name.upper()],
            'dimension': dimension,
            'sections': dict(sections),
        })
        return context

        
class LibraryResourceView(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(templates, 'resource.html')
    
    def get_context_data(self, resource_id, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        resource = models.Resource.objects.get(pk=resource_id)
        dimension = resource.dimension
        resources = models.Resource.objects.filter(subcategory__dimension=dimension)
        sections = defaultdict(list)
        for resource in resources:
            sections[resource.subcategory].append(resource)
        context.update({
            'coach': COACHES[dimension.name.upper()],
            'dimension': dimension,
            'sections': dict(sections),
            'resource': resource,
            'resource_embed': mark_safe(resource.embed) if resource.embed else '',
            'resource_url': resource.url if not resource.url.endswith('example.com') else ''
        })
        return context
