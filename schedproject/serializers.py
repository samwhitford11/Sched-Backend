from schedules.models import Sched
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our TodoSerializer
class SchedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Sched
        # the fields that should be included in the serialized output
        fields = ['id', 'title', 'date', 'time']