import uuid
from django.db import models

from api.models import User


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    monthly_budget = models.IntegerField(default=0)
    colour_hex = models.CharField(max_length=9)
    icon = models.CharField(max_length=100)
    household = models.ForeignKey('Household', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
