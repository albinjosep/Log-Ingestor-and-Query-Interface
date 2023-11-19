# log_app/models.py
from django.db import models

class Log(models.Model):
    level = models.CharField(max_length=50)
    message = models.TextField()
    resourceId = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    traceId = models.CharField(max_length=50)
    spanId = models.CharField(max_length=50)
    commit = models.CharField(max_length=50)
    parentResourceId = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        app_label = 'log_app'
