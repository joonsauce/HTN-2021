from django.db import models
import uuid


class Users(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250)
    num = models.CharField(max_length=2)
