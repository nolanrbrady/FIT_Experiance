from enum import Enum


def jsonify(data):
    return [i.to_dict() for i in data]


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
            return ((i.value, i.name) for i in cls)


class SubCategoryScore(object):

    def __init__(self, SubCategory=None, Score=None, ShortTermValue=None, Color=None, Description='', Weight=None):
        self.SubCategory = SubCategory # SubCategory
        self.Score = Score # decimal
        self.ShortTermValue = ShortTermValue # decimal
        self.Color = Color # string
        self.Description = Description # string
        self.Weight = Weight # double

    def to_dict(self):
        return dict(
            # "SubCategory": {"Multiplier": 5, "Id": 1, "CategoryId": 1, "Name": "Learning Strategies"}
            SubCategory = {
                "Id": self.SubCategory.id,
                "Name": self.SubCategory.name,
                "Multiplier": self.SubCategory.multiplier,
                "CategoryId": self.SubCategory.dimension.id,
            },
            Score = self.Score,
            ShortTermValue = self.ShortTermValue,
            Color = self.Color,
            Description = self.Description,
            Weight = self.Weight if self.Weight else 0,
        )

class DimensionScores(object):
    
    def __init__(self, Dimension, DimScore, SubCatScores):
        self.Dimension = Dimension # Dimension
        self.DimScore = DimScore # Decimal
        self.SubCatScores = SubCatScores # List<SubCategoryScore> 


class DimensionScore(object):
    
    def __init__(self, Dimension, Score):
        self.Dimension = Dimension
        self.Score = Score


class OverviewData(object):

    def __init__(self, id = "cognitive", order = 1, score = 15.0, color = "#FFB163", label="Cognitive", weight = 0.5, balance = 1.00, subScores = []):
        self.id = id
        self.order = order
        self.score = score
        self.color = color
        self.label = label
        self.weight = weight
        self.balance = balance
        self.subScores = subScores
        self.rampingUp = ''
        self.developer = ''
        self.experienced = ''
        self.FITastic = ''
    
    @property
    def subscores(self):
        # unusual case choice
        return self.subScores
                 
    def to_dict(self):
        return {
            "id": self.id,
            "order": self.order,
            "score": self.score,
            "color": self.color,
            "label": self.label, 
            "weight": self.weight,
            "balance": self.balance,
            "subScores": [s.to_dict() for s in self.subScores],
            "rampingUp": self.rampingUp,
            "developer": self.developer,
            "experienced": self.experienced,
            "FITastic": self.FITastic,
        }
