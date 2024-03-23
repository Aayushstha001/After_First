from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Company(models.Model):
    company_name = models.CharField(max_length=255, unique=True)
    company_email = models.EmailField(max_length=255, unique=True)
    company_telephone1 = models.CharField(max_length=20, unique=True)
    company_telephone2 = models.CharField(max_length=20, unique=True)
    company_registration_no = models.CharField(max_length=7, unique=True)
    company_address = models.CharField(max_length=255)
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
        return self.branch_code
    
class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    post = models.CharField(max_length=255, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    employee_code = models.CharField(max_length=8, unique=True, null=True, blank=True)
    phone_no = models.CharField(max_length=15, unique=True, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='employee', null=True, blank=True)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class CompanyPost(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='company_post', null=True, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    
class EmployeePost(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='employee_post', null=True, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title