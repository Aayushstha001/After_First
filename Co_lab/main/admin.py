from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Employee)
admin.site.register(CompanyPost)
admin.site.register(EmployeePost)

class EmployeeInline(admin.StackedInline):
    model = Employee

class UserAdmin(admin.ModelAdmin):
    model = User
    field = '__all__'
    inlines = [EmployeeInline]

admin.site.unregister(User)

admin.site.register(User, UserAdmin)