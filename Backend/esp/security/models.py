import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models


class AlertLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=400, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    response = JSONField(default=dict, null=True)
    status = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "alert_log"
