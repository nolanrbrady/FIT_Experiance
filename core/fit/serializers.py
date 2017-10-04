from django.contrib.auth.models import User, Group
from portal.core.fit.models import Goal, Task, Progress
from portal.core.fit.models import Agenda, Objective, Plan
from portal.core.fit.models import Dimension, SubCategory
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class DimensionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dimension
        fields = ('id', 'name')


class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'dimension')
        
    dimension = DimensionSerializer()


class GoalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goal
        fields = ('text', 'subcategory')

    subcategory = SubCategorySerializer()


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('text', 'goal')
    
    goal = GoalSerializer()


class AgendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agenda
        fields = ('id', 'open', 'active', 'user')
    
    user = UserSerializer() 


class ObjectiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Objective
        fields = ('id', 'user')
    
    user = UserSerializer()


class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'start', 'end', 'task', 'objective', 'created', 'modified')
    
    task =  TaskSerializer()
    objective = ObjectiveSerializer()

