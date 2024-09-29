from rest_framework import viewsets, permissions

from api.models import Category, Household
from api.serializers.category_serializer import CategorySerializer
from api.viewsets.mixins import HouseholdViewsetMixin


class CategoryViewSet(HouseholdViewsetMixin):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
