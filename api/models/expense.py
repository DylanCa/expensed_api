import uuid
from django.contrib.auth.models import User
from django.db import models

from api.models.household import Household

class PaymentType(models.Model):
    name = models.CharField(max_length=255)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=10)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)

class Merchant(models.Model):
    name = models.CharField(max_length=255)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)

class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    date = models.DateField()
    location = models.CharField(max_length=255, null=True, blank=True)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)

