from __future__ import print_function
from django.core.management.base import BaseCommand, CommandError
from collections import namedtuple

from portal.core.fit import models
from portal.core.fit.models.questions import Question
from portal.core.fit.models.dimensions import Dimension
from portal.core.fit.models.dimensions import SubCategory
from portal.core.fit.models.scores import ScoreColor
from portal.core.fit.models.objectives import Goal, Task
from portal.core.fit.models.dreambuilder import Principle

from .data import subcategories, dimensions, goals, questions, tasks, colors 
from .data import principles
from .data import dreambuilder

# TODO: strip/clean input text on goals, tasks, questions, etc.

"""
with open('data/<file>.py') as f:
    for n, line in enumerate(f):
        if "\xe2" in line:
            print n, ':', line
"""

class Command(BaseCommand):
    help = 'Initialize FIT DB with default data'

    def handle(self, *args, **options):
        self._load_dimensions()
        self._load_subcategories()
        self._load_dim_colors()
        self._load_questions()
        self._load_goals()
        self._load_tasks()
        self._load_principles()
        self._load_dreambuilder()
        self.stdout.write(self.style.NOTICE('Remember to run sqlsequencereset!'))
        
    def _null(self, value, default):
        return default if value == None else value
    
    def _load_principles(self):
        
        for _n, item in enumerate(principles.rows, start=1):
            r, created = Principle.objects.get_or_create(
                id = _n,
                text = item,
            )
            if created:
                r.save()
        n = Principle.objects.count()
        self.stdout.write(self.style.SUCCESS('Successfully initialized %i of %i principles.' % (n, _n)))
    
    def _load_dim_colors(self):
        Row = namedtuple('Row', colors.cols)
        for vals in colors.rows:
            i = Row(*vals)
            r = ScoreColor(
                group = i.group,
                low = i.low,
                medium = i.medium,
                high = i.high,
                max = i.max
            )
            r.dimension = Dimension.objects.get(pk=i.dimension)
            r.save()
    
    def _load_dimensions(self):
        for _n, line in enumerate(dimensions.text):
            if _n == 0:
                Item = namedtuple('Item', [s.strip() for s in line.split('|')])
                print(', '.join(Item._fields))
            else:
                try:
                    vals = [v if v != 'NULL' else None for v in line.split('|')]
                    i = Item(*vals)
                    r = Dimension(
                        id = i.Id,
                        name = i.Name,
                        divisor = i.Divisor,
                        description = self._null(i.Description, ''),
                    )
                    r.save() 
                except Exception as e:
                    print(e)
                    print(_n,':',line)
        n = Dimension.objects.count()
        self.stdout.write(self.style.SUCCESS('Successfully initialized %i of %i questions.' % (n, _n)))
    
    def _load_subcategories(self):
        for _n, line in enumerate(subcategories.text):
            if _n == 0:
                Item = namedtuple('Item', [s.strip() for s in line.split('|')])
                print(', '.join(Item._fields))
            else:
                vals = [v if v != 'NULL' else None for v in line.split('|')]
                i = Item(*vals)
                r = SubCategory(
                    id = i.Id,
                    name = i.Name,
                    multiplier = i.Multiplier,
                )
                r.dimension = Dimension.objects.get(pk=i.CategoryId)
                r.save()
        n = SubCategory.objects.count()
        self.stdout.write(self.style.SUCCESS('Successfully initialized %i of %i subcategories.' % (n, _n)))
        
    def _load_questions(self):
        for _n, line in enumerate(questions.text):
            if _n == 0:
                Item = namedtuple('Item', [s.strip() for s in line.split('|')])
                print(', '.join(Item._fields))
            else:
                try:
                    vals = [v if v != 'NULL' else None for v in line.split('|')]
                    item = Item(*vals)
                    q = Question(
                        id = item.Id,
                        seq = item.Sequence,
                        content = item.QuestionContent,
                        is_reversed = item.IsReversed,
                        is_active = item.IsActive,
                        is_corp = item.IsCorp,
                        weight = item.Weight,
                        style = item.QuestionTypeId,
                    )
                    if item.DimensionId:
                        q.dimension = Dimension.objects.get(pk=item.DimensionId)
                    if item.CategoryId:
                        q.subcategory = SubCategory.objects.get(pk=item.CategoryId)
                    q.save()
                except Exception as e:
                    print(e)
                    print(_n,':',line)
        n = Question.objects.count()
        self.stdout.write(self.style.SUCCESS('Successfully initialized %i of %i questions.' % (n, _n)))
    
    def _load_goals(self):
        for _n, line in enumerate(goals.text):
            if _n == 0:
                Item = namedtuple('Item', [s.strip() for s in line.split('|')])
                print(', '.join(Item._fields))
            else:
                try:
                    vals = [v if v != 'NULL' else None for v in line.split('|')]
                    item = Item(*vals)
                    entry = Goal(
                        id = item.Id,
                        text = item.GoalString,
                    )
                    if item.SubDimensionId:
                        entry.subcategory = SubCategory.objects.get(pk=item.SubDimensionId)
                    entry.save()
                except Exception as e:
                    print(e)
                    print(_n,':',line)
        n = Goal.objects.count()
        self.stdout.write(self.style.SUCCESS('Successfully initialized %i of %i goals.' % (n, _n)))
    
    def _load_tasks(self):
        for _n, line in enumerate(tasks.text):
            if _n == 0:
                Item = namedtuple('Item', [s.strip() for s in line.split('|')])
                print(', '.join(Item._fields))
            else:
                try:
                    vals = [v if v != 'NULL' else None for v in line.split('|')]
                    item = Item(*vals)
                    entry = Task(
                        id = item.Id,
                        text = item.TaskString,
                    )
                    if item.GoalId:
                        entry.goal = Goal.objects.get(pk=item.GoalId)
                    entry.save()
                except Exception as e:
                    print(e)
                    print(_n,':',line)
        n = Task.objects.count()
        self.stdout.write(self.style.SUCCESS('Successfully initialized %i of %i tasks.' % (n, _n)))
    
    def _load_dreambuilder(self):
        for _n, item in enumerate(dreambuilder.purposes, start=1):
            purpose = models.dreambuilder.Purpose(**item)
            purpose.active = True
            purpose.save()
        n = models.dreambuilder.Purpose.objects.count()
        self.stdout.write(self.style.SUCCESS('Successfully initialized %i of %i purposes.' % (n, _n)))
