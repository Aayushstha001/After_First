from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.db.models import Q

def home(request):
    company_post = CompanyPost.objects.all()
    employee_post = EmployeePost.objects.all()

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    companies = Company.objects.filter(
        Q(company_name__icontains=q)
    )

    r = request.GET.get('r') if request.GET.get('r') != None else ''
    users = User.objects.filter(
        Q(username__icontains=r) |
        Q(email__icontains=r) |
        Q(first_name__icontains=r) |
        Q(last_name__icontains=r) 
    )

    employees = Employee.objects.all()

    try:
        if request.user.is_authenticated:
            employee = Employee.objects.get(user=request.user)
        else:
            employee = {}
    except:
        employee ={} 

    context = {'employee': employee, 'company_post': company_post, 'employee_post': employee_post, 'companies': companies, 'users': users, 'employees': employees}
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about_us.html', {})

def register_user(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
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

@login_required(login_url='login')
def create_company_post(request):
    form = CompanyPostForm(request.POST, request.FILES)
    user = User.objects.get(username=request.user)
    employee = Employee.objects.get(user=user)
    company = employee.company

    if request.method == "POST":
        form = CompanyPostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                companypost = form.save(commit=False)
                companypost.host = request.user
                companypost.company = company
                companypost.save()
                return redirect('home')
            except Exception as e:
                messages.error(request, f'Error occurred during post: {e}')
        else:
            messages.error(request, 'Error occurred during post.')

    context = {'form': form} 
    return render(request, 'main/company_post_form.html', context)   

@login_required(login_url='login')
def delete_company_post(request, pk):
    post = CompanyPost.objects.get(id=pk)

    if request.user != post.host:
        return HttpResponse('You cannot delete this room!')
    
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    
    return render(request, 'main/delete.html', {'obj':post})

@login_required(login_url='login')
def create_employee_post(request):
    form = EmployeePostForm(request.POST, request.FILES)

    if request.method == "POST":
        form = EmployeePostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                employeepost = form.save(commit=False)
                employeepost.host = request.user
                employeepost.save()
                return redirect('home')
            except Exception as e:
                messages.error(request, f'Error occurred during post: {e}')
        else:
            messages.error(request, 'Error occurred during post.')

    context = {'form': form} 
    return render(request, 'main/employee_post_form.html', context) 

@login_required(login_url='login')
def delete_employee_post(request, pk):
    post = EmployeePost.objects.get(id=pk)

    if request.user != post.host:
        return HttpResponse('You cannot delete this room!')

    if request.method == 'POST':
        post.delete()
        return redirect('home')
    
    return render(request, 'main/delete.html', {'obj':post})

def userProfile(request, pk):
    user = User.objects.get(id=pk) 
    employee = user.employee  
    if employee:
        employee_post = user.employeepost_set.all()  
    else:
        employee = None
        employee_post = None
    context = {'user': user, 'employee_post': employee_post, 'employee': employee}  
    return render(request, 'main/user_profile.html', context)

def companyProfile(request, pk):
    company = Company.objects.get(id=pk)
    company_post = company.companypost_set.all()
    branch = company.branch_set.all()
    context={'company': company, 'company_post': company_post, 'branch': branch}
    return render(request, 'main/company_profile.html', context)