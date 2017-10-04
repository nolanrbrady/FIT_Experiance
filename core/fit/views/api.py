from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from portal.core.fit.models import Goal, Task, Progress
from portal.core.fit.models import Agenda, Objective, Plan
from portal.core.fit.models import Dimension, SubCategory
from portal.core.fit.permissions import IsAdminOrIsSelf
from portal.core.fit.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DimensionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Dimension.objects.all()
    serializer_class = DimensionSerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class AgendaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer


class ObjectiveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Objective.objects.all()
    serializer_class = ObjectiveSerializer
    
    
class PlanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    
    @detail_route(methods=['post'], permission_classes=[IsAdminOrIsSelf])
    def schedule(self, request, pk=None):
        plan = Plan.objects.get(pk=pk)
        plan.start = request.data['startsAt']
        plan.end = request.data['endsAt']
        plan.save()
        return Response({"ok":True})


