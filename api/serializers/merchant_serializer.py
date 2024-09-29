from rest_framework import serializers

from api.models import Merchant
from api.serializers.mixins import HouseholdSerializerMixin


class MerchantSerializer(HouseholdSerializerMixin):
    parent_lookup_kwargs = {
        "household_pk": "household__pk",
    }

    class Meta:
        model = Merchant
        fields = '__all__'
        read_only_fields = ['user', 'household']

