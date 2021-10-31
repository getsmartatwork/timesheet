from django.db import models

# Create your models here.
from accountant.models import Client,Vendor


class ProjectEmployee(models.Model):
    timesheet_type_choices = (
        ('weekly', 'weekly'),
        ('biweekly', 'biweekly'),
        ('monthly', 'monthly'),        
    )
    user_code = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True) 
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)
    max_hours_per_week = models.IntegerField()
    timesheet_type = models.CharField(choices=timesheet_type_choices, max_length=30)
    organization_code = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.employee_name)


class TimeSheetSet(models.Model):
    timesheet_status_choices = (
        ('saved', 'saved'),
        ('submitted', 'submitted'),
        ('approved', 'approved'),        
        ('reverted', 'reverted'),        
        ('locked', 'locked'),        
    )
    project = models.ForeignKey(ProjectEmployee, on_delete=models.CASCADE)
    total_hours = models.IntegerField()
    timesheet_status = models.CharField(choices=timesheet_status_choices, max_length=30)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.total_hours)

class TimeSheetAttachemnts(models.Model):
    attachment = models.FileField(upload_to='attachments', blank=True, null=True)
    timesheet_set = models.ForeignKey(TimeSheetSet, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.timesheet_set.total_hours)


class TimeSheet(models.Model):
    timesheet_set = models.ForeignKey(TimeSheetSet, on_delete=models.CASCADE)
    date = models.DateField()
    hours = models.IntegerField()

    def __str__(self):
        return "{}".format(self.date)

