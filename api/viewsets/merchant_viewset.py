from rest_framework import viewsets, permissions

from api.models import Merchant
from api.serializers.merchant_serializer import MerchantSerializer
from api.viewsets.mixins import HouseholdViewsetMixin


class MerchantViewSet(HouseholdViewsetMixin):
    queryset = Merchant.objects.all().order_by('id')
    serializer_class = MerchantSerializer
    permission_classes = [permissions.IsAuthenticated]
