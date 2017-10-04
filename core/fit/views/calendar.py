import os
import json
import pytz
import uuid
import datetime as dt
import icalendar
from icalendar import Calendar, Event
from django.contrib.sites.models import Site
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
from django.http import JsonResponse, HttpResponse
from django.http import HttpResponseRedirect
from django.conf import settings

import portal.core.fit.models as models
import portal.core.fit.sample as sample
import portal.core.fit.utils as utils
import portal.core.fit.calc as calc

from . import base

APP_PATH = os.path.join(base.APP_PATH, 'calendar')


class CalendarDetailsView(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'calendar_details.html')
    
    def get_context_data(self, id, **kwargs):
        context = super(CalendarDetailsView, self).get_context_data(**kwargs)    
        plan = models.Plan.objects.get(pk=id)
        start = plan.start if plan.start else dt.datetime.now()
        gcal_fmt = "https://www.google.com/calendar/render?action=TEMPLATE&text={text}&dates={start}/{end}&details={description}"
        gcal_url = gcal_fmt.format(
            text = plan.text,
            description = plan.description,
            start = start.strftime('%Y%m%dT%H%M%SZ'),
            end = (start + dt.timedelta(hours=1)).strftime('%Y%m%dT%H%M%SZ'),
        )
        # "https://www.google.com/calendar/render?action=TEMPLATE&text=Example+Event&dates=20161215T180000Z/20171215T220000Z&details=Some+content%0A+%0AMore+words&location=1821+30th+St,+Boulder,+CO,+80301"
        context.update({
            'plan_id': plan.id,
            'plan_brief': plan.text, 
            'dimension': plan.dimension,
            'subcategory': plan.subcategory,
            'gcal_url': gcal_url,
        })
        return context
 
 
class CalendarICS(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'calendar_details.html')
    
    def get_context_data(self, id, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        plan = models.Plan.objects.get(pk=id)
        context.update({
            'plan':plan,
        })
        return context
        
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        
        default_date = dt.date.today()
        
        user = request.user
        
        plan = context['plan']
        
        cal = Calendar()
        site = Site.objects.get_current()
        
        cal.add('prodid', '-//%s Events Calendar//%s//' % (site.name, site.domain))
        cal.add('version', '2.0')
        
        site_token = site.domain.split('.')
        site_token.reverse()
        site_token = '.'.join(site_token)
    
        ical_event = Event()
        ical_event.add('summary', plan.text)
        ical_event.add('dtstart', plan.start)
        ical_event.add('dtend', plan.end and plan.end or plan.start)
        ical_event.add('dtstamp', plan.end and plan.end or plan.start)
        ical_event['uid'] = '%d.event.events.%s' % (plan.id, site_token)
        
        if user.account.timezone:
            tz = pytz.timezone(user.account.timezone)
        else:
            # TODO do something reasonable  
            tz = pytz.timezone("US/Mountain") 
        reminderHours = 1
        startHour = 11
        start = tz.localize(dt.datetime.combine(default_date, dt.time(startHour, 0, 0)))
        cal = icalendar.Calendar()
        cal.add('prodid', '-//%s Assistant//%s//' % (site.name, site.domain))
        cal.add('version', '2.0')
        
        cal.add('method', "REQUEST")
        event = icalendar.Event()
        event.add('organizer', user.email)
        event.add('status', "confirmed")
        event.add('category', "Event")
        event.add('summary', plan.text)
        event.add('description', plan.description)
        #event.add('location', "location")
        event.add('dtstart', start)
        event.add('dtend', tz.localize(dt.datetime.combine(default_date, dt.time(startHour + 1, 0, 0))))
        event.add('dtstamp', tz.localize(dt.datetime.combine(default_date, dt.time(6, 0, 0))))
        event['uid'] = uuid.uuid4()
        event.add('priority', 5)
        event.add('sequence', 1)
        event.add('created', tz.localize(dt.datetime.now()))
        
        alarm = icalendar.Alarm()
        alarm.add("action", "DISPLAY")
        alarm.add('description', "Reminder")
        alarm.add("trigger", dt.timedelta(hours=-reminderHours))
        # The only way to convince Outlook to do it correctly
        alarm.add("TRIGGER;RELATED=START", "-PT{0}H".format(reminderHours))
        event.add_component(alarm)
        
        cal.add_component(event)
        response = HttpResponse(cal.to_ical(), content_type="text/calendar")
        response['Content-Disposition'] = 'attachment; filename=%s.ics' % plan.id
        return response


 
class CalendarView(LoginRequiredMixin, base.IndexView):
    template_name = os.path.join(APP_PATH, 'calendar.html')
    
    def get_context_data(self, **kwargs):
        context = super(CalendarView, self).get_context_data(**kwargs)
        try:
            agenda = models.Agenda.objects.filter(user=self.request.user, active=True).latest()
        except models.Agenda.DoesNotExist:
            agenda, created = models.Agenda.objects.get_or_create(
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
                start = plan.start if plan.start else dt.datetime.now()
                lst.append({
                    'id': str(plan.id),
                    'task': task.text,
                    'goal': obj.goal.text,
                    'subcategory': obj.subcategory.name,
                    'dimension': obj.subcategory.dimension.name,
                    'start': start.isoformat(),
                    'end': (start + + dt.timedelta(hours=1)).isoformat(),
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


