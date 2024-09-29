from rest_framework import serializers

from api.models import Household


class HouseholdSerializerMixin(serializers.ModelSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs = self.validate_household(attrs)
        attrs = self.validate_user(attrs)

        return attrs

    def validate_household(self, attrs):
        household = self.get_household()
        attrs["household"] = household

        return attrs

    def validate_user(self, attrs):
        user = self.get_user()
        attrs["user"] = user

        return attrs

    def get_household(self):
        household_pk = self.context["view"].kwargs['household_pk']
        return Household.objects.get(id=household_pk)

    def get_user(self):
        return self.context["request"].user


