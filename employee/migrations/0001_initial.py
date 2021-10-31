# Generated by Django 3.2.8 on 2021-10-31 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accountant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_code', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.CharField(blank=True, max_length=400, null=True)),
                ('user_code', models.CharField(max_length=100)),
                ('employee_name', models.CharField(max_length=100)),
                ('start_date', models.DateField(auto_now=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('max_hours_per_week', models.IntegerField()),
                ('timesheet_type', models.CharField(choices=[('weekly', 'weekly'), ('biweekly', 'biweekly'), ('monthly', 'monthly')], max_length=30)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accountant.client')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accountant.vendor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeSheetSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_code', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.CharField(blank=True, max_length=400, null=True)),
                ('total_hours', models.IntegerField()),
                ('timesheet_status', models.CharField(choices=[('saved', 'saved'), ('submitted', 'submitted'), ('approved', 'approved'), ('reverted', 'reverted'), ('locked', 'locked')], max_length=30)),
                ('comments', models.TextField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.projectemployee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeSheetAttachemnts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(blank=True, null=True, upload_to='attachments')),
                ('timesheet_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.timesheetset')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hours', models.IntegerField()),
                ('timesheet_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.timesheetset')),
            ],
        ),
    ]
