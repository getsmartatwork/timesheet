from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import permissions
from .models import ProjectEmployee, TimeSheetSet, TimeSheetAttachemnts, TimeSheet
from .serializers import ProjectEmployeeSerializer, TimeSheetSetSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProjectEmployeeViewSet(viewsets.ModelViewSet):
    queryset = ProjectEmployee.objects.all()
    serializer_class = ProjectEmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['organization_code', 'user_code']

class TimeSheetSetViewSet(viewsets.ModelViewSet):
    queryset = TimeSheetSet.objects.all()
    serializer_class = TimeSheetSetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['project']

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(doctor=self.request.user.profile.doctor)
        return self.queryset


    def create(self, request, *args, **kwargs):
        isError = False
        responseException = None

        try:
            request.data
            response_data = {'message':'added successfully',"responseException":responseException,'isError':isError}
            return Response(response_data, status=status.HTTP_200_OK)


        except Exception as e:
            isError = True
            responseException =  "{}".format(e)
            return Response({"responseException":responseException,'isError':isError}, status=status.HTTP_400_BAD_REQUEST)



