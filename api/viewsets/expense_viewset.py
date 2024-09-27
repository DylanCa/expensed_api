from rest_framework import viewsets, permissions

from api.models.expense import Expense, PaymentType, Category, Merchant
from api.serializers.expense_serializer import ExpenseSerializer, PaymentTypeSerializer, CategorySerializer, \
    MerchantSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Expense.objects.filter(household=self.kwargs['household_pk'])

class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all().order_by('id')
    serializer_class = PaymentTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PaymentType.objects.filter(household=self.kwargs['household_pk'])

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(household=self.kwargs['household_pk'])

class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all().order_by('id')
    serializer_class = MerchantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Merchant.objects.filter(household=self.kwargs['household_pk'])
