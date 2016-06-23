from rest_framework import serializers
from .models import Task


class TasksSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = (
        'id', 'name', 'scheduled_date_time'
        )
