from __future__ import print_function
import os
import json
from django.core.management.base import BaseCommand, CommandError
from collections import namedtuple
from django.contrib.auth.models import User
from portal.core.fit import models
from portal.core.fit import calc


class Command(BaseCommand):
    help = 'Export FIT Assessments'
    
    def add_arguments(self, parser):
        parser.add_argument('email_to', nargs='+', type=str)
        
    def handle(self, *args, **options):
        data_dir = 'data'
        delimiter = '\t'
        cols = []
        filename = os.path.join('data','survey_questions.tsv')        
        with open(filename,'w') as f:
            f.write(delimiter.join(['qid','question']) + '\n')
            for qid, question in self._questions():
                cols.append(qid)
                f.write(delimiter.join([qid, question.content]) + '\n')
        filename = os.path.join(data_dir, 'survey_answers.tsv') 
        with open(filename,'w') as f:
            f.write(delimiter.join(['Email'] + cols) + '\n')
            for row in self._answers():
                f.write(delimiter.join(map(str,row)) + '\n')
        
        filename = os.path.join('data','survey_scores.tsv')        
        with open(filename,'w') as f:
            cols, rows = self._scores()
            f.write(delimiter.join(cols) + '\n')
            for row in rows:
                f.write(delimiter.join(map(str,row)) + '\n')
        self._subscores(data_dir, delimiter)
        
    def _questions(self):
        mat = calc.SurveyMatrix()
        for qid, question in mat.questions():
            print(',\t'.join((qid, question.content)))
            yield (qid, question)
    
    def _answers(self, latest_only=True):
        lst = []
        _num = 0
        _users = set()
        questionCount = models.Question.objects.exclude(dimension__isnull=True).count()
        lookup = {question.content: qid for qid, question in self._questions()}
        cols = sorted(lookup.values())
        for user in User.objects.all():
            name = "{} {}".format(user.first_name, user.last_name)
            print('#', user.email, name)
            try:
                survey = None
                for _n, chk in enumerate(models.Survey.objects.filter(user=user, is_active=False).order_by('modified'), start=1):
                    num_answers = models.Answer.objects.filter(survey=chk).count()
                    print(_n, num_answers, chk.id, chk.modified)
                    if num_answers == questionCount:
                        survey = chk
                        _num += 1
                        _users.add(user)
                if survey is None:
                    raise models.Survey.DoesNotExist
                else:
                    vals = {}
                    for answer in models.Answer.objects.filter(survey=survey):
                        qid = lookup[answer.question.content]
                        vals[qid] = answer.value
                    row = [user.email]
                    row.extend([vals[qid] for qid in cols])
                    yield row
            except models.Survey.DoesNotExist:
                print('No survey for {}'.format(user))
    
    def _scores(self):
        _num = 0
        _users = set()
        matrix = calc.SurveyMatrix()
        cols = ['Email']
        cols.extend([d.name for d in matrix.dimensions()])
        rows = []
        questionCount = models.Question.objects.exclude(dimension__isnull=True).count()
        for user in User.objects.all():
            print('#', user.first_name, user.last_name, user)
            try:
                survey = None
                for _n, chk in enumerate(models.Survey.objects.filter(user=user, is_active=False).order_by('modified'), start=1):
                    num_answers = models.Answer.objects.filter(survey=chk).count()
                    print(_n, num_answers, chk.id, chk.modified)
                    if num_answers == questionCount:
                        survey = chk
                        _num += 1
                        _users.add(user)
                if survey is None:
                    raise models.Survey.DoesNotExist
                data = calc.UsersAnswers.scores(user, survey)
                for item in data:
                    print(json.dumps(item.to_dict(), indent=4))
                _tmp = {v.id: v.score for v in data}
                row = [user.email]
                row.extend([_tmp[col.lower()] for col in cols[1:]])
                rows.append(row)
            except models.Survey.DoesNotExist:
                print('No survey for {}'.format(user))
        return cols, rows
    
    def _subscores(self, data_dir, delimiter):
        matrix = calc.SurveyMatrix()
        cols, rows, xref = matrix.subscores()
        print(cols, rows, xref)
        filename = os.path.join('data','survey_subcategories.tsv')
        with open(filename, 'w') as f:
            for id, text in sorted(((v,k) for k,v in xref.items())):
                f.write(delimiter.join((id, text)) + '\n')
                print(id, text)
        filename = os.path.join('data','survey_subscores.tsv')        
        with open(filename,'w') as f:
            f.write(delimiter.join(cols) + '\n')
            for row in rows:
                f.write(delimiter.join(map(str,row)) + '\n')
                
