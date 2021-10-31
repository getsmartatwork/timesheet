
from rest_framework import serializers
from .models import Client, Vendor

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id','client_name','organization_code','status')


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id','vendor_name','organization_code','status')