from rest_framework import permissions

from api.models import PaymentType
from api.serializers.payment_serializer import PaymentTypeSerializer
from api.viewsets.mixins import HouseholdViewsetMixin


class PaymentTypeViewSet(HouseholdViewsetMixin):
    queryset = PaymentType.objects.all().order_by('id')
    serializer_class = PaymentTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
