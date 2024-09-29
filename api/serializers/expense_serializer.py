from rest_framework import serializers

from api.models import Expense
from api.serializers.mixins import HouseholdSerializerMixin


class ExpenseSerializer(HouseholdSerializerMixin):
    class Meta:
        model = Expense
        fields = '__all__'



