from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import permissions
from .models import Client, Vendor
from .serializers import ClientSerializer, VendorSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['organization_code']

    # permission_classes = [permissions.IsAuthenticated]
    # def get_queryset(self):
    #     if self.action == 'list':
    #         return self.queryset.filter(doctor=self.request.user.profile.doctor)
    #     return self.queryset

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['organization_code']