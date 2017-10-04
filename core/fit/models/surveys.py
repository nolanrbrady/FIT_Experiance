from django.db import models
from django.conf import settings
from django.contrib import admin
from portal.core.fit.utils import ChoiceEnum


class SurveyType(ChoiceEnum):
    Free = 1
    Indivdual = 2
    Corporate = 3


class Survey(models.Model):
    
    class Meta:
        get_latest_by = 'modified'
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_active = models.BooleanField(default=True)
    is_corp = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return 'Survey %s:' % self.user


class SurveyQuestion(models.Model):
    
    survey = models.ForeignKey("Survey")
    question = models.ForeignKey("Question")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


admin.site.register(Survey)
admin.site.register(SurveyQuestion)

"""
class DemographicView(models.Model):

    string Password { get; set; }
    int UserId { get; set; }
    string FirstName { get; set; }
    string LastName { get; set; }
    string Email { get; set; }
    string Gender { get; set; }
    string MaritalStatus { get; set; }
    DateTime DateOfBirth { get; set; }
    

class MySurveysView(models.Model):

    int SurveyId { get; set; }
    DateTime CreateDate { get; set; }
    decimal FitScore { get; set; }
    decimal BalanceScore { get; set; }
    decimal cognitiveScore { get; set; }
    decimal FinancialScore { get; set; }
    decimal EmotionalScore { get; set; }
    decimal PhysicalScore { get; set; }


class SurveyView(models.Model):

    List<Dimension> Dimensions { get; set; }
    List<SubCategory> SubCategories { get; set; }
    List<Question> Questions { get; set; }
    int SurveyId { get; set; }
    List<Answer> Answers { get; set; }


class SurveyTemplate(models.Model):

    int SurveyId { get; set; }
    int SurveyTypeId { get; set; }
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
"""
