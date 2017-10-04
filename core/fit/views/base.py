import os
import logging
from enum import Enum
from django.views.generic.base import TemplateView
from django.conf import settings
import portal.core.fit.models as models

APP_PATH = 'core/fit'

logger = logging.getLogger('fit')

class SurveyStatus(Enum):
    NONE = 0
    CREATED = 1
    PARTIAL = 2
    COMPLETE = 3
    ERROR = 4


class IndexView(TemplateView):
    template_name = os.path.join(APP_PATH, 'index.html')
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        try:
            context['MIXPANEL_TOKEN'] = settings.MIXPANEL_TOKEN
        except:
            pass
        user = self.request.user
        context['SURVEY_NONE'] = SurveyStatus.NONE
        context['SURVEY_CREATED'] = SurveyStatus.CREATED
        context['SURVEY_PARTIAL'] = SurveyStatus.PARTIAL
        context['SURVEY_COMPLETE'] = SurveyStatus.COMPLETE
        context['SURVEY_ERROR'] = SurveyStatus.ERROR
        context['SURVEY_STATUS'] = SurveyStatus.NONE
        if not user.is_anonymous():
            status, created = models.Status.objects.get_or_create(user=user)
            # FIXME move this mess elsewhere
            try:
                survey = models.Survey.objects.filter(user=user).latest()
                context['latest_survey'] = survey  
            except models.Survey.DoesNotExist:
                survey = None
            if survey:
                answerCount = models.Answer.objects.filter(survey=survey).count()
                if answerCount == 0:
                     context['SURVEY_STATUS'] = SurveyStatus.CREATED
                else:
                    questionCount = models.Question.objects.exclude(dimension__isnull=True).count()
                    if answerCount < questionCount:
                        print(answerCount, questionCount)
                        context['SURVEY_STATUS'] = SurveyStatus.PARTIAL
                    elif answerCount == questionCount:
                        context['SURVEY_STATUS'] = SurveyStatus.COMPLETE
                        status.dashboard = True
                        status.save()
                    else:
                        context['SURVEY_STATUS'] = SurveyStatus.ERROR
            logger.info("SURVEY_STATUS = {} for {}".format(context['SURVEY_STATUS'], user))
            context['status'] = status
        return context
