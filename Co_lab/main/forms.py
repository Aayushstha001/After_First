from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'password1': PasswordInput(attrs={'class': 'form-control'}),
            'password2': PasswordInput(attrs={'class': 'form-control'}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'name', 'branch', 'employee_code', 'phone_no', 'address', 'image', 'company', 'admin', 'post']
        widgets = {
            'phone_no': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'company_email', 'company_telephone1', 'company_telephone2', 'company_registration_no', 'company_address', 'company_logo', 'company_description', 'date_established', 'company_social_website']
        widgets = {
            'date_established': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class CompanyPostForm(ModelForm):
    class Meta:
        model = CompanyPost
        fields = '__all__'
        exclude = ['host', 'company']

class EmployeePostForm(ModelForm):
    class Meta:
        model = EmployeePost
        fields = '__all__'
        exclude = ['host', 'company']