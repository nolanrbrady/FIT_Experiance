from django.db import models


class FitScore(models.Model):
    {
        public int Id { get; set; }
        public int UserId { get; set; }
        public int SubCategoryId { get; set; }
        public decimal Score { get; set; }
        public int SurveyId { get; set; }
        public decimal Balance { get; set; }
        public decimal CognitiveFit { get; set; }
        public decimal CognitiveBal { get; set; }
        public decimal EmotionalFit { get; set; }
        public decimal EmotionalBal { get; set; }
        public decimal PhysicalFit { get; set; }
        public decimal PhysicalBal { get; set; }
        public decimal FinancialFit { get; set; }
        public decimal FinancialBal { get; set; }
        public DateTime CreateDate { get; set; }
    }
