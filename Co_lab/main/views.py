from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, EmployeeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

def home(request):
    return render(request, 'main/home.html', {})

def about(request):
    return render(request, 'main/about_us.html', {})

def register_user(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('register_employee')
        else:
            messages.error(request, 'Error occurred during registration.')
    return render(request, 'main/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return render(request, 'main/login.html')
    else:
        return render(request, 'main/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def register_employee(request):
    form = EmployeeForm()
    companies = Company.objects.all()
    branches = Branch.objects.all()

    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                employee = form.save(commit=False)
                employee.user = request.user
                employee.branch = Branch.objects.get(pk=request.POST['branch'])
                employee.company = Company.objects.get(pk=request.POST['company']) 
                employee.save()
                messages.success(request, 'Employee registered successfully.')
                return redirect('home')
            except Exception as e:
                messages.error(request, f'Error occurred during registration: {e}')
        else:
            messages.error(request, 'Error occurred during registration.')

    context = {'form': form, 'companies': companies, 'branches': branches}
    return render(request, 'main/employee_register.html', context)
