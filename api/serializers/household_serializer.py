from rest_framework import serializers
from api.models.expense import Household

class HouseholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Household
        fields = ['id', 'name', 'members']
        read_only_fields = ['id']
