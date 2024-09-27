from rest_framework import viewsets

from api.models.household import Household
from api.serializers.household_serializer import HouseholdSerializer


class HouseholdViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Household.objects.all().order_by('id')
    serializer_class = HouseholdSerializer