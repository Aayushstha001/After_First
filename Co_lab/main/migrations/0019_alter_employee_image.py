# Generated by Django 4.2.7 on 2024-03-24 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_companypost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, default='avatar.png', null=True, upload_to='employee'),
        ),
    ]
