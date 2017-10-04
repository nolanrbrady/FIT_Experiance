from django.db import models
from django.contrib import admin
from django.conf import settings


class ScoreColor(models.Model):
    
    dimension = models.OneToOneField('Dimension', primary_key=True, on_delete=models.CASCADE)
    group = models.TextField(blank=True, max_length=10, help_text='red, blue, green, etc.')
    low = models.TextField(max_length=7, help_text='score < 10')
    medium = models.TextField(max_length=7, help_text='score >= 10 && score < 15')
    high = models.TextField(max_length=7, help_text='score >= 15 && score < 20')
    max = models.TextField(max_length=7, help_text='score >= 20')
    
    def __str__(self):
        return "%s: %s" % (self.dimension, self.group)

admin.site.register(ScoreColor)

"""
class DimensionScore(models.Model):
    
    dimension = models.ForeignKey('Dimension')
    score = models.DecimalField()


class FitScore(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL) 
    subcategory = models.ForeignKey('SubCategory')
    score = models.DecimalField()
    survey = models.ForeignKey('Survey')
    balance = models.DecimalField()
    cognitive_fit = models.DecimalField(default=0)
    cognitive_bal = models.DecimalField(default=0)
    emotional_fit = models.DecimalField(default=0)
    emotional_bal = models.DecimalField(default=0)
    physical_fit = models.DecimalField(default=0)
    physical_bal = models.DecimalField(default=0)
    financial_fit = models.DecimalField(default=0)
    financial_bal = models.DecimalField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)



public class ShortTermValue
    {        
        public decimal Answer { get; set; }
    }


public class SubCategoryScore
    {
        public SubCategory SubCategory { get; set; }

        public decimal Score { get; set; }
        public decimal ShortTermValue { get; set; }
        public string Color { get; set; }
        public string Description { get; set; }
        public double Weight { get; set; }
    }


public class EffortWeight
    {
        //public Dimension Dimension { get; set; }
        //public SubCategory SubCategory { get; set; }
        public decimal Weight { get; set; }
    }

public class DimensionScores
    {
        public Dimension Dimension { get; set; }
        public decimal DimScore { get; set; }
        public List<SubCategoryScore> SubCatScores { get; set; }
    }


public class FutureStateData
    {        
        public decimal FutureBalance { get; set; }

        public decimal FutureFit { get; set; }       

        public List<SubCategoryScore> FutureSubCategories { get; set; }
    }


public class FutureStates
    {
        public List<DimensionScore> FutureDimensions { get; set; }
        public List<SubCategoryScore> FutureSubCatScores { get; set; }
        public decimal FutureFitScore { get; set; }
        public decimal FutureBalanceScore { get; set; }

    }
"""
