from __future__ import unicode_literals
from django.db import models

from libs.models import TimeStampedModel


class Task(TimeStampedModel):
  name = models.CharField(max_length=512)
  scheduled_date_time = models.DateTimeField(blank=True)
  class Meta:
    ordering = ('scheduled_date_time',)

