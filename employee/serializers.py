
from rest_framework import serializers
from .models import ProjectEmployee, TimeSheetSet

class ProjectEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectEmployee
        # depth = 1
        fields = ('id','user_code','organization_code','employee_name','start_date','end_date','client','vendor','max_hours_per_week','timesheet_type')


class TimeSheetSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSheetSet
        fields = ('id','project','total_hours','timesheet_status','comments')