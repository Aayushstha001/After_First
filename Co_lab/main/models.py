from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Company(models.Model):
    company_name = models.CharField(max_length=255, unique=True)
    company_email = models.EmailField(max_length=255, unique=True)
    company_telephone1 = models.CharField(max_length=20, unique=True)
    company_telephone2 = models.CharField(max_length=20, unique=True)
    company_registration_no = models.CharField(max_length=7, unique=True)
    company_address = models.CharField(max_length=255, unique=True)
    company_logo = models.ImageField(upload_to='company', null=True, blank=True)
    company_description = models.TextField()
    date_established = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    company_social_website = models.URLField(max_length=200)

    def __str__(self):
        return self.company_name
    
class Branch(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=255)
    branch_code = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.branch_name
    
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    employee_code = models.CharField(max_length=8, unique=True)
    phone_no = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='employee', null=True, blank=True)

    def __str__(self):
        return self.user.username