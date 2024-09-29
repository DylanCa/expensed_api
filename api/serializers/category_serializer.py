from rest_framework import serializers

from api.models import Category
from api.serializers.mixins import HouseholdSerializerMixin


class CategorySerializer(HouseholdSerializerMixin):
    parent_lookup_kwargs = {
        "household_pk": "household__pk",
    }

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['user', 'household']