from .models import itemDetails, offerTypeAndValue, myOrder
from rest_framework import serializers


class itemDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = itemDetails
        fields = ['id', 'name', 'quantity', 'price']


class OfferTypeAndValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = offerTypeAndValue
        fields = ['id', 'type', 'offerValue']

class myOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = myOrder
        fields = ['id', 'distance']