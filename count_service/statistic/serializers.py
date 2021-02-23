from rest_framework import serializers
from .models import *

class StatisticCounterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StatisticCounter
        fields = {'date','views','clicks','cost'}