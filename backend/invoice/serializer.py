from rest_framework import serializers
from .models import *


class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ("desc", "rate", "quantity")


class InvoiceSerializer(serializers.ModelSerializer):
    items = itemSerializer(many=True)

    class Meta:
        model = Invoices
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
