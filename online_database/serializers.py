from rest_framework import serializers
from .models import Customer

class CustomerQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name",
                  "last_name",
                  "city",
                  "state",
                  "email_address",
                  "phone_number",)