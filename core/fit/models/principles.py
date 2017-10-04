from django.db import models


public class Principle:IEntity
    public int DreamBuilderId { get; set; }
    public string PrincipleText { get; set; }
    public bool IsSelected { get; set; }


public class PrincipleAnswer(models.Model):

        public int Id { get; set; }
        public int DreamBuilderId { get; set; }
        public string PrincipleAnswerText { get; set; }
        public int PrincipleId { get; set; }


public class PrincipleList
    {
        public static List<string> List
        {
            get
            { return (new string[] { 
                    "Character",
                    "Civic Engagement",
                    "Commitment",
                    "Common Sense",
                    "Compassion",
                    "Connection",
                    "Courage",
                    "Courtesy",
                    "Curiosity",
                    "Dedication",
                    "Effort",
                    "Empathy",
                    "Flexibility",
                    "Forgiveness",
                    "Fortitude",
                    "Friendship",
                    "Grit",
                    "Honesty",
                    "Humanitarianism",
                    "Humility",
                    "Integrity",
                    "Justice",
                    "Kindness",
                    "Loyalty",
                    "Optimism",
                    "Patience",
                    "Perseverance",
                    "Problem-Solving",
                    "Resiliency",
                    "Responsibility",
                    "Self-Discipline",
                    "Service",
                    "Sincerity",
                    "Teamwork",
                    "Temperance",
                    "Trust",
           }).ToList();
            }
        }
    }
