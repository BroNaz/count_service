from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import viewsets, permissions

from .models import StatisticCounter
from .serializers import StatisticCounterSerializer

# Create your views here.
class StatisticSaveView(viewsets.ModelViewSet):
    queryset = StatisticCounter.objects.all()
    serializer_class = StatisticCounterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
