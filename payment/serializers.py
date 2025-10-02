from rest_framework import serializers

class MockPaymentRequestSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    force_failed = serializers.BooleanField()

class MockPaymentResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    gateway_response = serializers.DictField()