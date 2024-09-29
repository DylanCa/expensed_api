import uuid
from django.db import models

from api.models import User


class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    household = models.ForeignKey('Household', on_delete=models.CASCADE)
    merchant = models.ForeignKey('Merchant', on_delete=models.CASCADE)
    payment_type = models.ForeignKey('PaymentType', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)

