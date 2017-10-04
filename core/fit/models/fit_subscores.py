from django.db import models


public class FitSubScore(models.Model):
    {
        public int Id { get; set; }
        public int UserId { get; set; }
        public decimal Score { get; set; }
        public int CategoryId { get; set; }
        public string Name { get; set; }
        public int FitScoreId { get; set; }
    }

