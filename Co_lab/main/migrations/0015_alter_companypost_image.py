# Generated by Django 4.2.7 on 2024-03-23 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_employee_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companypost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='companypost'),
        ),
    ]
