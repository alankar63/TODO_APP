from __future__ import unicode_literals
from django.db import models
from libs.models import TimeStampedModel
from datetime import datetime, timedelta
from users.models import User

class Task(TimeStampedModel):
  name = models.CharField(max_length=512)
  scheduled_date_time = models.DateTimeField(default=(datetime.now() + timedelta(weeks=52)), blank=True)
  pending = models.BooleanField(default=True)
  last_updated = models.DateTimeField(default=datetime.now, blank=True)
  user = models.ForeignKey(User, default='1')  # remove default afterwards

  class Meta:
    ordering = ('scheduled_date_time',)

