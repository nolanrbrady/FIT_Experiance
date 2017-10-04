"""atk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib import admin
from rest_framework import routers
from portal.core.fit.views import api
 
from .views.base import IndexView

from .views import BioIleneRuskView
from .views import BioJamesDoranView
from .views import BioJimLeightonView
from .views import BioLaurenLeightonView
from .views import BioRenaKirklandView
from .views import BioShaneNiemeyerView

from .views import DimCognitiveView
from .views import DimEmotionalView
from .views import DimFinancialView
from .views import DimPhysicalView

from .views import AccountView
from .views import AssessmentView
from .views import IndividualSurveyView
from .views import DemographicView
from .views import WelcomeView
from .views import SaveAnswer
from .views import FitScore
from .views import FitButtonCheck
from .views import HomeView

from .views.dashboard import DashboardView

from .views.calendar import CalendarView
from .views.calendar import CalendarDetailsView
from .views.calendar import CalendarICS

from .views.library import LibraryDimensionView
from .views.library import LibraryResourceView

from .views.dreambuilder import DreamBuilderView
from .views.dreambuilder import DreamEnvironment
from .views.dreambuilder import DreamPurposeView
from .views.dreambuilder import DreamPrinciplesView
from .views.dreambuilder import SaveEnvironment
from .views.dreambuilder import UpdatePurpose
from .views.dreambuilder import SaveDefinedPrinciples
from .views.dreambuilder import SaveVisionView
from .views.dreambuilder import SavePurposeAnswers
from .views.dreambuilder import UpdatePrinciple
from .views.dreambuilder import DreamDefPrinciplesView
from .views.dreambuilder import DreamVisionView
from .views.dreambuilder import DreamReportView
from .views.dreambuilder import DreamStatementView
from .views.dreambuilder import SavePurposeStatement

from .views.planbuilder import PlanBuilder
from .views.planbuilder import PlanBuilderObjects
from .views.planbuilder import PlanBuilderGoals
from .views.planbuilder import PlanBuilderAgenda
from .views.planbuilder import PlanObjects
from .views.planbuilder import AddObjective
from .views.planbuilder import RemoveObjective
from .views.planbuilder import LoadGoals
from .views.planbuilder import GetDimension
from .views.planbuilder import GetSubCategory
from .views.planbuilder import LoadTasks
from .views.planbuilder import AddTask
from .views.planbuilder import RemoveTask
from .views.planbuilder import ClearTasks

from .views import UsersAnswers
from .views import AllSurveysAnswer


router = routers.DefaultRouter()
router.register(r'^users', api.UserViewSet)
router.register(r'^groups', api.GroupViewSet)
router.register(r'^dimensions', api.DimensionViewSet)
router.register(r'^subcategories', api.SubCategoryViewSet)
router.register(r'^objectives', api.ObjectiveViewSet)
router.register(r'^agendas', api.AgendaViewSet)
router.register(r'^plans', api.PlanViewSet)


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),


    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    url(r'^about/$', TemplateView.as_view(template_name='core/fit/home/about.html'), name='about'),
    
    url(r'^bios/ilene_rusk', BioIleneRuskView.as_view(), name='bio_ilene_rusk'),
    url(r'^bios/Ilene_Rusk', BioIleneRuskView.as_view(), name='bio_ilene_rusk'),
    url(r'^bios/james_doran', BioJamesDoranView.as_view(), name='bio_james_doran'),
    url(r'^bios/James_Doran', BioJamesDoranView.as_view(), name='bio_james_doran'),
    url(r'^bios/jim_leighton', BioJimLeightonView.as_view(), name='bio_jim_leighton'),
    url(r'^bios/Jim_Leighton', BioJimLeightonView.as_view(), name='bio_jim_leighton'),
    url(r'^bios/lauren_leighton', BioLaurenLeightonView.as_view(), name='bio_lauren_leighton'),
    url(r'^bios/rena_kirkland', BioRenaKirklandView.as_view(), name='bio_rena_kirkland'),
    url(r'^bios/Rena_Kirkland', BioRenaKirklandView.as_view(), name='bio_rena_kirkland'),
    url(r'^bios/shane_niemeyer', BioShaneNiemeyerView.as_view(), name='bio_shane_niemeyer'),
    url(r'^bios/Shane_Niemeyer', BioShaneNiemeyerView.as_view(), name='bio_shane_niemeyer'),

    url(r'^bios/', IndexView.as_view(), name='coach_bio'),
    
    url(r'^[Cc]ognitive', DimCognitiveView.as_view(), name='cognitive'),
    url(r'^[Ee]motional', DimEmotionalView.as_view(), name='emotional'),
    url(r'^[Ff]inancial', DimFinancialView.as_view(), name='financial'),
    url(r'^[Pp]hysical', DimPhysicalView.as_view(), name='physical'),
    
    url(r'^plan-builder/$', PlanBuilder.as_view(), name='plan_builder'),
    url(r'^plan-builder/objects/$', PlanBuilderObjects.as_view(), name='planbuilder_objects'),
    url(r'^plan/builder/objects/$', PlanBuilderObjects.as_view(), name='plan_builder_objects'),
    url(r'^plan/goals/$', PlanBuilderGoals.as_view(), name='plan_builder_goals'),
    url(r'^plan/agenda/$', PlanBuilderAgenda.as_view(), name='plan_builder_agenda'),
    url(r'^plan/objects/$', PlanObjects.as_view(), name='plan_objects'),
    url(r'^plan/AddPlanBuilderObject/$', AddObjective.as_view(), name='plan_create'),
    url(r'^plan/RemovePlanBuilderObject/$', RemoveObjective.as_view(), name='plan_remove'),
    url(r'^plan/LoadGoals/$', LoadGoals.as_view(), name='plan_load_goals'),
    url(r'^plan/GetDimension/$', GetDimension.as_view(), name='plan_get_dimension'),
    url(r'^plan/GetSubCategory/$', GetSubCategory.as_view(), name='plan_get_sub_category'),
    url(r'^plan/load-tasks/$', LoadTasks.as_view(), name='plan_load_Tasks'),
    url(r'^plan/add-task/$', AddTask.as_view(), name='plan_add_task'),
    url(r'^plan/remove-task/$', RemoveTask.as_view(), name='plan_remove_task'),
    url(r'^plan/clear-tasks/$', ClearTasks.as_view(), name='plan_clear_tasks'),
    
    url(r'^dream-builder/$', DreamBuilderView.as_view(), name='dream_builder'),
    url(r'^dream-builder/environment$', DreamEnvironment.as_view(), name='dreambuilder_environment'),
    url(r'^dream-builder/SaveEnvironment$', SaveEnvironment.as_view(), name='SaveEnviroment'),
    url(r'^dream-builder/purpose/$', DreamPurposeView.as_view(), name='dreambuilder_purpose'),

    url(r'^dream-builder/UpdatePurpose/$', UpdatePurpose.as_view(), name='dreambuilder_update'),
    
    url(r'^dreambuilder/UpdatePrinciple/$', UpdatePrinciple.as_view(), name='dreambuilder_updateprinciple'),
    
    url(r'^dream-builder/purpose/SavePurposeAnswers/$', SavePurposeAnswers.as_view(), name='SavePurposeAnswers'),
    url(r'^dream-builder/principles$', DreamPrinciplesView.as_view(), name='dreambuilder_principles'),
    url(r'^dream-builder/defineprinciples$', DreamDefPrinciplesView.as_view(), name='dreambuilder_defineprinciples'),
    
    url(r'^dream-builder/SaveDefinedPrinciples/$', SaveDefinedPrinciples.as_view(), name='SaveDefinedPrinciples'),
    url(r'^dream-builder/vision/$', DreamVisionView.as_view(), name='dreambuilder_vision'),
    
    url(r'^dream-builder/statement/$', DreamStatementView.as_view(), name='dreambuilder_statement'),
    
    url(r'^dream-builder/statement/SavePurposeStatement/$', SavePurposeStatement.as_view(), name='SavePurposeStatement'),
    
    url(r'^dream-builder/vision/SaveVision/$', SaveVisionView.as_view(), name='dreambuilder_savevision'),
    
    url(r'^dream-builder/report/$', DreamReportView.as_view(), name='dreambuilder_report'),
    
    url(r'^library/$', TemplateView.as_view(template_name='core/fit/library/index.html'), name='library'),
    url(r'^library/dimension/(?P<dimension_id>[-\w]+)/$', LibraryDimensionView.as_view(), name='library_dimension'),
    url(r'^library/resource/(?P<resource_id>[-\w]+)/$', LibraryResourceView.as_view(), name='library_resource'),

    url(r'^calendar/export/(?P<id>[-\w]+)/$', CalendarICS.as_view(), name="calendar_export"),
    
    url(r'^calendar/details/(?P<id>[-\w]+)/$', CalendarDetailsView.as_view(), name='calendar_details'),
    
    url(r'^calendar/$', CalendarView.as_view(), name='calendar'),
    
    url(r'^upgrade/$', IndexView.as_view(template_name='core/fit/dashboard.html'), name='upgrade'),
    
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),

    url(r'^demo/$', TemplateView.as_view(template_name='core/fit/demo.html'), name='demo'),
    url(r'^demo_p1/$', TemplateView.as_view(template_name='core/fit/demo_p1.html'), name='demo_p1'),
    url(r'^demo_p2/$', TemplateView.as_view(template_name='core/fit/demo_p2.html'), name='demo_p2'),
    url(r'^demo_p3/$', TemplateView.as_view(template_name='core/fit/demo_p3.html'), name='demo_p3'),
    url(r'^demo_p4/$', TemplateView.as_view(template_name='core/fit/demo_p4.html'), name='demo_p4'),
    url(r'^demo_p5/$', TemplateView.as_view(template_name='core/fit/demo_p5.html'), name='demo_p5'),
    url(r'^demo_p6/$', TemplateView.as_view(template_name='core/fit/demo_p6.html'), name='demo_p6'),

    url(r'^privacy_policy/$', TemplateView.as_view(template_name='core/fit/privacy_policy.html'), name='privacy_policy'),
    url(r'^termsofservice/$', TemplateView.as_view(template_name='core/fit/termsofservice.html'), name='termsofservice'),


    url(r'^history/$', DashboardView.as_view(), name='history'),
    
    url(r'^secure/account/$', AccountView.as_view(template_name='core/fit/secure/account.html'), name='account'),
    
    url(r'^secure/GetAllSurveysAnswer/$', AllSurveysAnswer.as_view(), name='secure_GetAllSurverysAnwser'),
    url(r'^secure/GetUsersAnwsers/$', UsersAnswers.as_view(), name='answers'),
    url(r'^secure/SaveFitScore/$', FitScore.as_view(), name='score'),
    
    url(r'^assessment/$', AssessmentView.as_view(template_name='core/fit/survey_update.html'), name='assessment'),  # New assesment
    
    url(r'^survey/answer/$', SaveAnswer.as_view(), name='survey_answer'),
    url(r'^survey/assessment/$', AssessmentView.as_view(), name='survey_assessment'),  # Continue assesment
    url(r'^survey/demographic/$', DemographicView.as_view(), name='survey_demographic'),
    url(r'^survey/individual/$', IndividualSurveyView.as_view(), name='survey_individual'),
    url(r'^survey/welcome/$', WelcomeView.as_view(), name='survey_welcome'),
    url(r'^survey/check/$', FitButtonCheck.as_view(), name='survey_check'),
    
    url(r'^dimension/cognitive/$', TemplateView.as_view(template_name='core/fit/dim_cognitive.html'), name='dim_cognitive'),
    url(r'^dimension/emotional/$', TemplateView.as_view(template_name='core/fit/dim_emotional.html'), name='dim_emotional'),
    url(r'^dimension/financial/$', TemplateView.as_view(template_name='core/fit/dim_financial.html'), name='dim_financial'),
    url(r'^dimension/physical/$', TemplateView.as_view(template_name='core/fit/dim_physical.html'), name='dim_physical'),
    
    url(r'^fitfor/leaders/$', TemplateView.as_view(template_name='core/fit/fitfor_leaders.html'), name='fitfor_leaders'),
    url(r'^fitfor/coaches/$', TemplateView.as_view(template_name='core/fit/fitfor_coaches.html'), name='fitfor_coaches'),
    url(r'^fitfor/individuals/$', TemplateView.as_view(template_name='core/fit/fitfor_individuals.html'), name='fitfor_individuals'),
    url(r'^fitfor/organizations/$', TemplateView.as_view(template_name='core/fit/fitfor_organizations.html'), name='fitfor_organizations'),
    
]

urlpatterns += [
    url(r'^search/', include('haystack.urls')),
]

