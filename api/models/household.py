import uuid
from django.db import models
from django.conf import settings

from api.models import User


class Household(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='households')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
