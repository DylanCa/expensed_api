from rest_framework import viewsets

from api.models import Household


class HouseholdViewsetMixin(viewsets.ModelViewSet):
    parent_queryset = Household.objects.all()
    parent_lookup_field = "pk"
    parent_lookup_url_kwarg = "household_pk"
    lookup_field = "pk"

    def get_queryset(self):
        filters = {}

        parent = self.get_parent()
        filters["household"] = parent.id

        return self.queryset.model.objects.filter(**filters).order_by("id")

    def get_parent(self):
        if "household_pk" in self.kwargs:
            return Household.objects.get(pk=self.kwargs["household_pk"])
        else:
            return None

    def perform_create(self, serializer):
        instance = serializer.save()
        parent = self.get_parent()

        return instance