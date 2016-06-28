from rest_framework import serializers
from .models import User
from tasks.serializers import TasksSerializer

class UsersSerializer(serializers.ModelSerializer):
  # tasks = TasksSerializer(many=True)
  class Meta:
    model = User
    fields = (
         'name', 'email', 'username', 'password',
        )
