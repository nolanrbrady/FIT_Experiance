import os
import json
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
from django.http import HttpResponseBadRequest
from django.conf import settings

import portal.core.fit.models as models
import portal.core.fit.sample as sample
import portal.core.fit.utils as utils
import portal.core.fit.calc as calc

from . import base

templates = os.path.join(base.APP_PATH, 'planbuilder')


class PlanBuilder(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(templates, 'planbuilder.html')
    
    def get_context_data(self, **kwargs):
        context = super(PlanBuilder, self).get_context_data(**kwargs)
        for agenda in models.Agenda.objects.filter(user = self.request.user, open = True, active = True).all():
            agenda.open = False
            agenda.save()
        agenda = models.Agenda(
            user = self.request.user,
            open = True,
            active = True,
        )
        agenda.save()
        context.update({ 'AgendaId': agenda.id })
        return context


class PlanBuilderGoals(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(templates, 'planbuilder_goals.html')
    
    def get_context_data(self, **kwargs):
        context = super(PlanBuilderGoals, self).get_context_data(**kwargs)    
        agenda = models.Agenda.objects.get(
            user = self.request.user,
            open = True,
            active = True,
        )
        objectives = models.Objective.objects.filter(agenda = agenda).all()
        # need to loop through objective -> tasks and divide into pairs (maybe)
        {"Id":242,"UserId":331,"GoalId":48,"Task1Id":0,"Task2Id":0,"DimensionId":3,"SubDimensionId":16}
        lst = []
        for obj in objectives:
            tasks = [plan.task for plan in obj.plan_set.all()]
            lst.append({
                'Id': str(obj.id),
                'UserId': obj.agenda.user.id,
                'GoalId': obj.goal.id,
                'TaskId': tasks[0].id if tasks else None,
                'Task2Id': tasks[1].id if len(tasks) > 1 else None,
                'DimensionId': obj.subcategory.dimension.id,
                'SubDimensionId': obj.subcategory.id,
            })
        context.update({
            'AgendaId': agenda.id,
            'PlanBuilderObjects': mark_safe(json.dumps(lst)),
        })
        return context


class PlanBuilderObjects(LoginRequiredMixin, View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        agenda = models.Agenda.objects.get(
            user = self.request.user,
            open = True,
            active = True,
        )
        objectives = models.Objective.objects.filter(agenda = agenda).all()
        # need to loop through objective -> tasks and divide into pairs (maybe)
        {"Id":242,"UserId":331,"GoalId":48,"Task1Id":0,"Task2Id":0,"DimensionId":3,"SubDimensionId":16}
        lst = []
        for obj in objectives:
            tasks = [plan.task for plan in obj.plan_set.all()]
            lst.append({
                'Id': str(obj.id),
                'UserId': obj.agenda.user.id,
                'GoalId': obj.goal.id,
                'TaskId': tasks[0].id if tasks else None,
                'Task2Id': tasks[1].id if len(tasks) > 1 else None,
                'DimensionId': obj.subcategory.dimension.id,
                'SubDimensionId': obj.subcategory.id,
            })
        return JsonResponse({'data':lst})



class PlanBuilderAgenda(LoginRequiredMixin, TemplateView):
    template_name = os.path.join(templates, 'planbuilder_agenda.html')
    
    def get_context_data(self, **kwargs):
        context = super(PlanBuilderAgenda, self).get_context_data(**kwargs)    
        agenda = models.Agenda.objects.get(
            user = self.request.user,
            open = True,
            active = True,
        )
        objectives = models.Objective.objects.filter(
            agenda = agenda
        ).all()
        # need to loop through objective -> tasks and divide into pairs (maybe)
        {"Id":242,"UserId":331,"GoalId":48,"Task1Id":0,"Task2Id":0,"DimensionId":3,"SubDimensionId":16}
        lst = []
        for obj in objectives:
            for plan in obj.plan_set.all():
                task = plan.task
                lst.append({
                    'id': str(plan.id),
                    'task': task.text,
                    'goal': obj.goal.text,
                    'subcategory': obj.subcategory.name,
                    'dimension': obj.subcategory.dimension.name,
                    'start': plan.start.isoformat() if plan.start else dt.datetime.now().isoformat(),
                    'end': plan.end.isoformat() if plan.end else dt.datetime.now().isoformat(),
                    'UserId': obj.agenda.user.id,
                    'GoalId': obj.goal.id,
                    'TaskId': str(task.id),
                    'DimensionId': obj.subcategory.dimension.id,
                    'SubDimensionId': obj.subcategory.id
                })
        context.update({
            'AgendaId': agenda.id,
            'PlanObjects': mark_safe(json.dumps(lst)),
        })
        return context


class PlanObjects(LoginRequiredMixin, View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        agenda = models.Agenda.objects.get(
            user = self.request.user,
            open = True,
            active = True,
        )
        objectives = models.Objective.objects.filter(
            agenda = agenda
        ).all()
        # need to loop through objective -> tasks and divide into pairs (maybe)
        {"Id":242,"UserId":331,"GoalId":48,"Task1Id":0,"Task2Id":0,"DimensionId":3,"SubDimensionId":16}
        lst = []
        ids = []
        for obj in objectives:
            ids.append(str(obj.id))
            for plan in obj.plan_set.all():
                task = plan.task
                lst.append({
                    'id': str(plan.id),
                    'task': task.text,
                    'goal': obj.goal.text,
                    'subcategory': obj.subcategory.name,
                    'dimension': obj.subcategory.dimension.name,
                    'start': plan.start.isoformat() if plan.start else dt.datetime.now().isoformat(),
                    'end': plan.end.isoformat() if plan.end else dt.datetime.now().isoformat(),
                    'UserId': obj.agenda.user.id,
                    'GoalId': obj.goal.id,
                    'TaskId': str(task.id),
                    'DimensionId': obj.subcategory.dimension.id,
                    'SubDimensionId': obj.subcategory.id
                })
        return JsonResponse({'data':lst,'objectives':ids})


class LoadGoals(LoginRequiredMixin, View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        _id = request.GET.get('SubcategoryId', None)
        if _id is None:
            return HttpResponseBadRequest("Missing required parameter: 'SubcategoryId'")
        subcategory = models.SubCategory.objects.get(pk=_id)
        lst = [{
            'Id': goal.id,
            'GoalString': goal.text,
            'SubDimensionId': _id,
        } for goal in models.Goal.objects.filter(subcategory = subcategory).all()]
        return JsonResponse(lst, safe=False)


class GetSubCategory(LoginRequiredMixin, View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        _id = request.GET.get('id', None)
        if _id is None:
            return HttpResponseBadRequest("Missing required parameter: 'id'")
        subcategory = models.SubCategory.objects.get(id=_id)
        return JsonResponse(subcategory.name, safe=False)


class GetDimension(LoginRequiredMixin, View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        _id = request.GET.get('id', None)
        if _id is None:
            return HttpResponseBadRequest("Missing required parameter: 'Id (cf. DimensionId)'")
        dimension = models.Dimension.objects.get(pk=_id)
        return JsonResponse(dimension.name, safe=False)


class LoadTasks(LoginRequiredMixin, View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        _id = request.GET.get('Id', None)
        if _id is None:
            return HttpResponseBadRequest("Missing required parameter: 'Id (cf. GoalId)'")
        goal = models.Goal.objects.get(pk=_id)
        lst = [{
            'Id': task.id,
            'GoalId': task.goal.id,
            'TaskString': task.text,
        } for task in models.Task.objects.filter(goal = goal).all()][::-1]
        return JsonResponse(lst, safe=False)

####

class AddTask(LoginRequiredMixin, View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        objective_id = request.GET.get('planbuilderObjectId')
        task_id = request.GET.get('taskId')
        goal_id = request.GET.get('goalId') # unnecessary cf. Objective
        plan, created = models.Plan.objects.get_or_create(
            objective = models.Objective.objects.get(pk=objective_id),
            task = models.Task.objects.get(pk=task_id),
        )
        return JsonResponse({"status":200,"title":"Success","PlanId": plan.id, "ObjectiveId":objective_id})


#
# /planbuilder/RemoveTask?planbuilderObjectId=203a31a3-943e-45ee-a009-2968e76a5957&taskId=454&goalId=58
#
class RemoveTask(LoginRequiredMixin, View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        objective_id = request.GET.get('planbuilderObjectId')
        task_id = request.GET.get('taskId')
        goal_id = request.GET.get('goalId') # unnecessary cf. Objective
        plan = models.Plan.objects.get(
            objective = models.Objective.objects.get(pk=objective_id),
            task = models.Task.objects.get(pk=task_id),
        )
        plan.delete()
        return JsonResponse({"status":200,"title":"Success","objective_id":objective_id})

#
# /planbuilder/ClearTasks?planbuilderObjectId=203a31a3-943e-45ee-a009-2968e76a5957
#         
class ClearTasks(LoginRequiredMixin, View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        _id = request.GET.get('planbuilderObjectId')
        objective = models.Objective.objects.get(pk=_id)
        for plan in objective.plan_set.all():
            plan.delete()
        return JsonResponse({"status":200,"title":"Success"})

####

class AddObjective(LoginRequiredMixin, View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        _id = request.GET.get('SubdimensionId',None)
        if _id is None:
            return JsonResponse({"status":400,"title":"Bad Request","SubdimensionId": None})
        # else
        agenda = models.Agenda.objects.get(
            user = request.user,
            open = True
        )
        subcategory = models.SubCategory.objects.get(pk=_id)
        goal = models.Goal.objects.filter(subcategory = subcategory).first()
        objective = models.Objective(
            user = request.user,
            agenda = agenda,
            subcategory = subcategory,
            goal = goal,
        )
        objective.save()
        return JsonResponse({"status":200,"title":"Success!","SubdimensionId": _id})


class RemoveObjective(LoginRequiredMixin, View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        _id = request.GET.get('SubdimensionId','1')
        return JsonResponse({"status":200,"title":"Success","SubdimensionId": _id})
