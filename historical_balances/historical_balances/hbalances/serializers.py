from . import models
from rest_framework import serializers

class HbalancesSerializer(serializers.Serializer):
    amount = serializers.IntegerField(required=False, read_only = False)
    currency = serializers.CharField(max_length=10, required=False, read_only = False)
    date = serializers.CharField(max_length=30, required=False, read_only = False)
    status = serializers.CharField(max_length=30, required=False, read_only = False)