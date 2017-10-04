from django.contrib import admin

import portal.core.fit.models as models


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','seq','content','dimension','subcategory','weight','style')


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id','created','modified','user','dashboard','history','agenda')


@admin.register(models.Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('id','created','modified','user','open','active')


@admin.register(models.Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ('id','created','modified','user')


@admin.register(models.Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('created','modified','start','end','user','task','goal','dimension')


@admin.register(models.library.Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('dimension','subcategory','title')

@admin.register(models.PurposeAnswer)
class PurposeAnswerAdmin(admin.ModelAdmin):
    list_display = ('id','purpose','text','active')


@admin.register(models.PrincipleAnswer)
class PrincipleAnswerAdmin(admin.ModelAdmin):
    list_display = ('id','label','text','active')


@admin.register(models.Vision)
class VisionAdmin(admin.ModelAdmin):
    list_display = ('id','title','text')

    
@admin.register(models.PurposeStatement)
class PurposeStatementAdmin(admin.ModelAdmin):
    list_display = ('id','text')

