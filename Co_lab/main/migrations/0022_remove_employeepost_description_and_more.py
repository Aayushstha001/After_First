# Generated by Django 4.2.7 on 2024-03-24 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_companypost_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeepost',
            name='description',
        ),
        migrations.AlterField(
            model_name='employeepost',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
