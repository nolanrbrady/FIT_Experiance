import os
from django.core.urlresolvers import reverse_lazy
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
import portal.core.fit.models as models

from . import base

APP_PATH = base.APP_PATH


class DashboardView(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'dashboard.html')
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        try:
            survey = models.Survey.objects.filter(user=request.user).latest() # FIXME
        except models.Survey.DoesNotExist:
            return HttpResponseRedirect(reverse_lazy('fit:survey_assessment'))
        return TemplateResponse(request, self.template_name, context=context)
