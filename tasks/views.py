from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TasksSerializer
from .models import Task


class TasksViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()
  serializer_class = TasksSerializer
