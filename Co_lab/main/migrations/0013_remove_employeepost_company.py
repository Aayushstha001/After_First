# Generated by Django 4.2.7 on 2024-03-23 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_employee_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeepost',
            name='company',
        ),
    ]
