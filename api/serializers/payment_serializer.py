from rest_framework import serializers

from api.models import PaymentType
from api.serializers.mixins import HouseholdSerializerMixin


class PaymentTypeSerializer(HouseholdSerializerMixin):
    parent_lookup_kwargs = {
        "household_pk": "household__pk",
    }

    class Meta:
        model = PaymentType
        fields = '__all__'
        read_only_fields = ['user', 'household']