import os
import json
import logging
import datetime as dt
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response, redirect
from django.views.generic.base import View, TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils.safestring import mark_safe
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.conf import settings

import portal.core.fit.models as models
import portal.core.fit.sample as sample
import portal.core.fit.utils as utils
import portal.core.fit.calc as calc

from . import base
from . import planbuilder


APP_PATH = base.APP_PATH


logger = logging.getLogger('fit')


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect(reverse_lazy('home'), permanent=True) 

#

class BioIleneRuskView(base.IndexView):
    template_name = os.path.join(APP_PATH, 'bio_ilene_rusk.html')
    
class BioJamesDoranView(base.IndexView):
    template_name = os.path.join(APP_PATH, 'bio_james_doran.html')

class BioJimLeightonView(base.IndexView):
    template_name = os.path.join(APP_PATH, 'bio_jim_leighton.html')

class BioLaurenLeightonView(base.IndexView):
    template_name = os.path.join(APP_PATH, 'bio_lauren_leighton.html')

class BioRenaKirklandView(base.IndexView):
    template_name = os.path.join(APP_PATH, 'bio_rena_kirkland.html')

class BioShaneNiemeyerView(base.IndexView):
    template_name = os.path.join(APP_PATH, 'bio_shane_niemeyer.html')

#

class DimCognitiveView(base.IndexView):
    template_name = os.path.join(APP_PATH, 'dim_cognitive.html')

class DimEmotionalView(base.IndexView):
    template_name = os.path.join(APP_PATH, 'dim_emotional.html')

class DimFinancialView(base.IndexView):
    template_name = os.path.join(APP_PATH, 'dim_financial.html')

class DimPhysicalView(base.IndexView):
    template_name = os.path.join(APP_PATH, 'dim_physical.html')

#

class AccountView(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'sec_account.html')


#

class HomeView(LoginRequiredMixin, FormView):
    template_name = os.path.join(APP_PATH, 'dashboard.html')
    success_url = reverse_lazy('thanks')
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['MIXPANEL_TOKEN'] = settings.MIXPANEL_TOKEN
        context['STRIPE_PUBLISHABLE'] = settings.STRIPE_PUBLISHABLE
        context['PLAID_ENVIRONMENT'] = settings.PLAID_ENVIRONMENT
        context['PLAID_PUBLIC_KEY'] = settings.PLAID_PUBLIC_KEY
        return context
    
    def form_valid(self, form):
        form.handle_charge(request=self.request)
        return super(HomeView, self).form_valid(form)


class FitScore(LoginRequiredMixin, View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(FitScore, self).dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        for survey in models.Survey.objects.filter(user=request.user, is_active=True):
            survey.is_active = False
            survey.save()
        return JsonResponse({"status":200,"message":"Success"}, safe=False)


class UsersAnswers(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        
        user = request.user
        
        cognitiveBool = request.GET.get("cognitive","0") == "1"
        financialBool = request.GET.get("financial","0") == "1"
        emotionalBool = request.GET.get("emotional","0") == "1"
        physicalBool = request.GET.get("physical","0") == "1"
        
        try:
            survey = None
            # TODO just mark survey complete already...
            questionCount = models.Question.objects.exclude(dimension__isnull=True).count()
            for _n, chk in enumerate(models.Survey.objects.filter(user=user, is_active=False).order_by('modified')):
                num_answers = models.Answer.objects.filter(survey=chk).count()
                print(_n, num_answers, chk.id, chk.modified)
                if num_answers == questionCount:
                    survey = chk
            if survey is None:
                 raise models.Survey.DoesNotExist
        except models.Survey.DoesNotExist:
            return HttpResponseRedirect(reverse_lazy('fit:survey_assessment'))
        
        data = calc.UsersAnswers.scores(user, survey, cognitiveBool, financialBool, emotionalBool, physicalBool)
        
        return JsonResponse(utils.jsonify(data), safe=False) # check sample.data


class AllSurveysAnswer(LoginRequiredMixin, View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AllSurveysAnswer, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return JsonResponse(sample.survey, safe=False)


class SaveAnswer(LoginRequiredMixin, View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SaveAnswer, self).dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        srv = models.Survey.objects.filter(user=request.user, is_active=True).order_by('-modified').first()
        if not srv:
            srv = models.Survey(user=request.user)
            srv.save()
        req = json.loads(request.body.decode('utf-8'))
        q = models.questions.Question.objects.get(pk=int(req['QuestionId']))
        ans, created = models.Answer.objects.get_or_create(survey=srv, question=q)
        if created:
            msg = 'Answer inserted'
        else:
            msg = 'Answer updated'
        ans.value = int(req.get('Value'))
        ans.save()
        return JsonResponse({"status":200,"title":"Success","message": msg})


class FitButtonCheck(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        text = ""
        link = ""
        
        try:
            survey = models.Survey.objects.filter(user=request.user).latest()
        except models.Survey.DoesNotExist:
            logger.error('Survey not found: {}'.format(request.user))
            survey = None
        
        questionCount = models.Question.objects.exclude(dimension__isnull=True).count()
        answerCount = models.Answer.objects.filter(survey=survey).count()
        
        if survey and questionCount != answerCount:
            link = reverse_lazy('fit:assessment')
            text = "Finish Assessment"
        else:
            link = reverse_lazy('fit:survey_assessment')
            text = "Take FIT Assessment"
        
        return JsonResponse({ 'status': 200, 'message': 'Success', 'text': text, 'link': link })

"""
{"Id":38026,"QuestionId":209,"UserId":361,"Value":3,"SurveyId":479},{"Id":38027,"QuestionId":2,"UserId":361,"Value":2,"SurveyId":479},{"Id":38028,"QuestionId":3,"UserId":361,"Value":3,"SurveyId":479},{"Id":38029,"QuestionId":4,"UserId":361,"Value":4,"SurveyId":479},{"Id":38030,"QuestionId":5,"UserId":361,"Value":3,"SurveyId":479},{"Id":38031,"QuestionId":6,"UserId":361,"Value":4,"SurveyId":479},{"Id":38032,"QuestionId":7,"UserId":361,"Value":4,"SurveyId":479},{"Id":38033,"QuestionId":9,"UserId":361,"Value":2,"SurveyId":479},{"Id":38034,"QuestionId":11,"UserId":361,"Value":3,"SurveyId":479},{"Id":38035,"QuestionId":13,"UserId":361,"Value":4,"SurveyId":479},{"Id":38036,"QuestionId":15,"UserId":361,"Value":3,"SurveyId":479}
"""

class AssessmentView(LoginRequiredMixin, base.IndexView):
    # override in urls for update/dashboard view
    template_name = os.path.join(APP_PATH, 'survey_assessment.html')
    
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        if context['SURVEY_STATUS'] == base.SurveyStatus.COMPLETE:
            survey = context.get('latest_survey')
            if survey:
                survey.is_active = False
                survey.save()
                try:
                    survey, created = models.Survey.objects.get_or_create(user=self.request.user, is_active=True)
                    if created:
                        context['SURVEY_STATUS'] = base.SurveyStatus.CREATED
                        logger.info('Created new survey for {}'.format(self.request.user))
                except models.Survey.MultipleObjectsReturned:
                    context['SURVEY_STATUS'] = base.SurveyStatus.PARTIAL
                    logger.info('Multiple active surveys for {}'.format(self.request.user))
                    survey = models.Survey.objects.filter(user=self.request.user, is_active=True).latest()
        if context['SURVEY_STATUS'] == base.SurveyStatus.PARTIAL:
            survey = context['latest_survey']
            context['latest_answers'] = mark_safe([
                {
                    "Id": ans.id,
                    "QuestionId": ans.question.id,
                    "UserId": survey.user.id,
                    "Value": ans.value,
                    "SurveyId": survey.id,
                } for ans in survey.answer_set.all()
            ])
        
        else:
            context['latest_answers'] = mark_safe([])
        return context



class IndividualSurveyView(LoginRequiredMixin ,base.IndexView):
    template_name = os.path.join(APP_PATH, 'survey_individual.html')


class DemographicView(base.IndexView):
    template_name = os.path.join(APP_PATH, 'survey_demographic.html')
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if not settings.FIT_ALLOW_ANONYMOUS:
            return HttpResponseRedirect(reverse_lazy('fit:survey_assessment'))
        return TemplateResponse(request, self.template_name, context=context)


class DemographicCreate(CreateView):
    
    model = models.demographics.Demographic
    fields = ['first_name','last_name','email','gender','date_of_birth','marital_status',]
    
    template_name = os.path.join(APP_PATH, 'survey_demographic.html')


class WelcomeView(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'survey_welcome.html')

