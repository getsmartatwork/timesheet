# Generated by Django 3.2.8 on 2021-10-31 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesheetset',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='timesheetset',
            name='modified_date',
        ),
        migrations.RemoveField(
            model_name='timesheetset',
            name='organization_code',
        ),
        migrations.RemoveField(
            model_name='timesheetset',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='timesheetset',
            name='status',
        ),
    ]
