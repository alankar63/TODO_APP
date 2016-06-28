from __future__ import unicode_literals
from django.db import models
from libs.models import TimeStampedModel


class User(TimeStampedModel):
  name = models.CharField(max_length=128, blank=False)
  username = models.CharField(max_length=128, blank=False, unique=True)
  email = models.EmailField(max_length=128, blank=False)
  # encrypt password afterwards
  password = models.CharField(max_length=128, blank=False, default='rooney')
  verified = models.BooleanField(default=False)

  class Meta:
    ordering = ('id',)

