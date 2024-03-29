# Generated by Django 4.2.7 on 2024-03-12 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=255)),
                ('branch_code', models.CharField(max_length=6, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, unique=True)),
                ('company_email', models.EmailField(max_length=255, unique=True)),
                ('company_telephone1', models.CharField(max_length=20, unique=True)),
                ('company_telephone2', models.CharField(max_length=20, unique=True)),
                ('company_registration_no', models.CharField(max_length=7, unique=True)),
                ('company_address', models.CharField(max_length=255, unique=True)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='company')),
                ('company_description', models.TextField()),
                ('date_established', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('company_social_website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_code', models.CharField(max_length=6, unique=True)),
                ('employee_code', models.CharField(max_length=8, unique=True)),
                ('phone_no', models.CharField(max_length=15, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='employee')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.branch')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.company'),
        ),
    ]
