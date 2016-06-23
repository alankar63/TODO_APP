from django.db import models


class TimeStampedModel(models.Model):
  install_ts = models.DateTimeField(auto_now_add=True)
  update_ts = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True
