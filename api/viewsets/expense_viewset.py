from rest_framework import viewsets, permissions

from api.models import Expense
from api.serializers.expense_serializer import ExpenseSerializer
from api.viewsets.mixins import HouseholdViewsetMixin


class ExpenseViewSet(HouseholdViewsetMixin):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
