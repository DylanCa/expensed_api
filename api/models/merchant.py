import uuid
from django.db import models

class Merchant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    household = models.ForeignKey('Household', on_delete=models.CASCADE)
