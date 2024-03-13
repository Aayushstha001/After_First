from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    context = {}
    return render(request, 'main/home.html', context)
    
def register_user(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('register_employee')
        else:
            messages.error(request, 'Error occured during registration')

    return render(request, 'main/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'main/login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'main/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def register_employee(request):
    form = EmployeeForm()

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            code = request.POST.get('branch_code')
            Employee.objects.create(
                user = request.user,
                company = request.POST.get('company'),
                branch = Branch.objects.get(branch_code=code),
                branch_code = code,
                employee_code = request.POST.get('employee_code'),
                phone_no = request.POST.get('phone_no'),
                image = request.POST.get('image'),
            )
            return redirect('home')
        else:
            messages.error(request, 'Error')
        
    context = {'form': form}
    return render(request, 'main/employee_register.html', context)