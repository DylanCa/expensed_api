from rest_framework import viewsets, permissions

from api.models import Household
from api.serializers.household_serializer import HouseholdSerializer


class HouseholdViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Household.objects.all().order_by('id')
    serializer_class = HouseholdSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Household.objects.filter(members__in=[self.request.user]).order_by("id")