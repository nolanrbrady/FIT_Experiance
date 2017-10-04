import os
import json
import logging
import requests
import datetime as dt
from collections import defaultdict, namedtuple
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

APP_PATH = os.path.join(base.APP_PATH, 'dreambuilder')

logger = logging.getLogger('fit')

#
# FIXME actual form handling...
# seems obvious now but didn't when I started
#


class DreamBuilderView(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'dreambuilder.html')


class DreamEnvironment(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'environment.html')
    
    def get(self, request, *args, **kwargs):
        context = super(DreamEnvironment, self).get_context_data(**kwargs)
        builder, created1 = models.DreamBuilder.objects.get_or_create(user=request.user)
        env, created2 = models.DreamEnviroment.objects.get_or_create(dreambuilder=builder)
        context.update({
            'NutrientPeople': env.nutrient_people,
            'ToxicPeople': env.toxic_people,
            'NutrientPlaces': env.nutrient_places,
            'ToxicPlaces': env.toxic_places,
            'NutrientResources': env.nutrient_resources,
            'ToxicResources': env.toxic_resources,
        })
        return TemplateResponse(request, self.template_name, context=context)


class DreamPurposeView(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'purpose.html')
    
    def get(self, request, *args, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        builder = models.DreamBuilder.objects.get(user=request.user)
        env, created = models.DreamEnviroment.objects.get_or_create(dreambuilder=builder)
        context.update({
            'NutrientPeople': env.nutrient_people,
            'ToxicPeople': env.toxic_people,
            'NutrientPlaces': env.nutrient_places,
            'ToxicPlaces': env.toxic_places,
            'NutrientResources': env.nutrient_resources,
            'ToxicResources': env.toxic_resources,
        })
        lst = []
        for purpose in models.Purpose.objects.order_by('id'):
            answer, created = models.PurposeAnswer.objects.get_or_create(dreambuilder=builder, purpose=purpose)
            lst.append({
                'Id': answer.purpose.id,
                'Question': answer.purpose.text,
                'Answer': answer.text,
                'IsChecked': json.dumps(answer.active),
                'PurposeId': answer.purpose.id,
                'AnswerId': answer.purpose.id,
                'Placeholder': answer.purpose.prompt
            })
        context.update({'Purposes': lst})
        return TemplateResponse(request, self.template_name, context=context)

            
class DreamPrinciplesView(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'principles.html')
    
    def get(self, request, *args, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        builder = models.DreamBuilder.objects.get(user=request.user)
        # TODO clever query
        answer_ids = set([ans.principle.id for ans in 
            models.PrincipleAnswer.objects.filter(dreambuilder=builder)
            if ans.active == True    
        ])
        lst = []
        Proxy = namedtuple('Proxy',['id','text','checked'])
        for principle in models.Principle.objects.order_by('id'):
            chk = 'checked="true"' if principle.id in answer_ids else ''
            proxy = Proxy(id=principle.id, text=principle.text, checked=chk)
            lst.append(proxy)
        context.update({'principles': lst})
        # TODO add already selected principles to PrinciplesCTRL init
        return TemplateResponse(request, self.template_name, context=context)


class UpdatePrinciple(LoginRequiredMixin, base.IndexView):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        id = body.get('Id', None)
        chk =  body.get('IsSelected', None)
        if id is not None and chk is not None:
            builder = models.DreamBuilder.objects.get(user=request.user)
            principle = models.Principle.objects.get(pk=id)
            answer, created = models.PrincipleAnswer.objects.get_or_create(
                dreambuilder=builder,
                principle=principle,
            )
            answer.active = chk
            answer.save()
            print('>', chk, answer.active)
        msg = "{} is checked".format(id)
        return JsonResponse({"message":"Success: {}".format(msg)})


class DreamDefPrinciplesView(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'defineprinciples.html')
    
    def get(self, request, *args, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        builder = models.DreamBuilder.objects.get(user=request.user)
        lst = []
        for principle in models.PrincipleAnswer.objects.filter(dreambuilder=builder, active=True).order_by('id'):
            lst.append(principle)
        context.update({'principles': lst})
        return TemplateResponse(request, self.template_name, context=context)


class SaveDefinedPrinciples(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'vision.html')
    
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        builder = models.DreamBuilder.objects.get(user=self.request.user)
        print(self.request.body, self.request.GET)
        for k,v in self.request.GET.items():
            if k.startswith('def:'):
                id = k.split(':')[1]
                ans = models.PrincipleAnswer.objects.get(pk=id)
                ans.text = v[0] if type(v) is list else v
                ans.save()
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return HttpResponseRedirect(reverse_lazy('fit:dreambuilder_vision'))


class DreamStatementView(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'statement.html')
    
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        builder = models.DreamBuilder.objects.get(user=self.request.user)
        answers = models.PurposeAnswer.objects.filter(dreambuilder=builder, active=True)
        statement, created = models.PurposeStatement.objects.get_or_create(dreambuilder=builder)
        context.update({
            'answers': answers, 
            'statement': statement,
            'remaining': 180-len(statement.text),
        })
        return context


class SavePurposeStatement(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'statement.html')
    
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        builder = models.DreamBuilder.objects.get(user=self.request.user)
        statement = models.PurposeStatement.objects.get(dreambuilder=builder)
        statement.text = self.request.GET.get('PurposeStatementString','')
        statement.save()
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return HttpResponseRedirect(reverse_lazy('fit:dreambuilder_principles'))


class DreamVisionView(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'vision.html')
    
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        builder = models.DreamBuilder.objects.get(user=self.request.user)
        vision, created = models.Vision.objects.get_or_create(dreambuilder=builder)
        context.update({
            'vision': vision,
        })
        return context


class SaveVisionView(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'report.html') # TODO forms forms forms
    
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        user = self.request.user
        builder = models.DreamBuilder.objects.get(user=user)
        vision, created = models.Vision.objects.get_or_create(dreambuilder=builder)
        print(self.request.body, self.request.GET)
        # {'Vision.Headline': ['better than nothing headline'], 'Vision.BodyText': ['Two']
        headline = self.request.GET['Vision.Headline']
        text = self.request.GET['Vision.BodyText']
        vision.title = headline if type(headline) is list else headline
        vision.text = text if type(text) is list else text
        vision.save()
        return context 

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return HttpResponseRedirect(reverse_lazy('fit:dreambuilder_report'))
    

class DreamReportView(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'report.html')
    
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        user = self.request.user
        builder = models.DreamBuilder.objects.get(user=user)
        principles = models.PrincipleAnswer.objects.filter(dreambuilder=builder, active=True)
        context.update({
            'principles': principles,
        })
        # wow... FIXME Quick!
        values = defaultdict(dict)
        try:
            survey = models.Survey.objects.filter(user=user, is_active=False).latest()
            data = calc.UsersAnswers.scores(user, survey) # returns utils.OverviewData
            for overview_data in data:
                dimension = overview_data.id
                # initial offset value: -13%
                score = int(round(overview_data.score))
                logger.info('Report: {} / {} = {}'.format(dimension, user.email, score))
                values[dimension]['score'] = score
                values[dimension]['bottom'] = round(score / 25 * 100) - 13
                values[dimension]['height'] = round(score / 25 * 100)
        except models.Survey.DoesNotExist:
            logger.error("Survey.DoesNotExist in SaveVisionView for {}".format(user))
        context.update({'prog':values})
        context.update({
            'vision': models.Vision.objects.get(dreambuilder=builder),
            'statement': models.PurposeStatement.objects.get(dreambuilder=builder),
            'environment': models.DreamEnviroment.objects.get(dreambuilder=builder),
        })
        env = models.DreamEnviroment.objects.get(dreambuilder=builder)
        nutrients = []
        nutrients.extend([env.nutrient_people])
        nutrients.extend([env.nutrient_places])
        nutrients.extend([env.nutrient_resources])
        toxins = []
        toxins.extend([env.toxic_people])
        toxins.extend([env.toxic_places])
        toxins.extend([env.toxic_resources])
        context.update({
            'nutrients': nutrients,
            'toxins': toxins,
        })
        return context


class SaveEnvironment(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'purpose.html')
    
    def post(self, request, *args, **kwargs):
        builder = models.DreamBuilder.objects.get(user=request.user)
        env = models.DreamEnviroment.objects.get(dreambuilder=builder)
        env.nutrient_people = request.POST.get('NutrientPeople')
        env.toxic_people = request.POST.get('ToxicPeople')
        env.nutrient_places = request.POST.get('NutrientPlaces')
        env.toxic_places = request.POST.get('ToxicPlaces')
        env.nutrient_resources = request.POST.get('NutrientResources')
        env.toxic_resources = request.POST.get('ToxicResources')
        env.save()
        return HttpResponseRedirect(reverse_lazy('fit:dreambuilder_purpose'))


class SavePurposeAnswers(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'principles.html')
    
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        builder = models.DreamBuilder.objects.get(user=self.request.user)
        for k, text in self.request.GET.items():
            print(k,text)
            name, id = k.split(',')
            purpose = models.Purpose.objects.get(pk=id)
            print(purpose)
            answer, created = models.PurposeAnswer.objects.get_or_create(
                dreambuilder = builder,
                purpose = purpose,
            )
            answer.text = text
            answer.active = True if text else False # FIXME angular needs to send IsChecked
            answer.save()
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return HttpResponseRedirect(reverse_lazy('fit:dreambuilder_statement'))


class UpdatePurpose(LoginRequiredMixin, base.IndexView):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        builder = models.DreamBuilder.objects.get(user=request.user)
        purpose = models.DreamEnviroment.objects.get(dreambuilder=builder)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        id = body.get('Id',None)
        msg = "{} is checked".format(id)
        return JsonResponse({"message":"Success: {}".format(msg)})

