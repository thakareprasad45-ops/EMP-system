from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EmployeeSignUpForm, EmployerSignUpForm, EmployeeProfileForm, CompanyForm, EmployerProfileForm
from .models import EmployeeProfile, EmployerProfile

def register_employee(request):
    if request.method == 'POST':
        form = EmployeeSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Employee account created successfully!")
            return redirect('employee_dashboard')
    else:
        form = EmployeeSignUpForm()
    return render(request, 'accounts/register.html', {'form': form, 'user_type': 'Employee'})

def register_employer(request):
    if request.method == 'POST':
        form = EmployerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Employer account created successfully!")
            return redirect('employer_dashboard')
    else:
        form = EmployerSignUpForm()
    return render(request, 'accounts/register.html', {'form': form, 'user_type': 'Employer'})

@login_required
def employee_profile(request):
    if not request.user.is_employee:
        return redirect('home')
    
    profile = request.user.employee_profile
    if request.method == 'POST':
        form = EmployeeProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('employee_profile')
    else:
        form = EmployeeProfileForm(instance=profile)
    return render(request, 'accounts/employee_profile.html', {'form': form})

@login_required
def employer_profile(request):
    if not request.user.is_employer:
        return redirect('home')
    
    profile = request.user.employer_profile
    company = profile.company
    
    if request.method == 'POST':
        c_form = CompanyForm(request.POST, request.FILES, instance=company)
        p_form = EmployerProfileForm(request.POST, instance=profile)
        if c_form.is_valid() and p_form.is_valid():
            c_form.save()
            p_form.save()
            messages.success(request, "Company and Profile updated successfully!")
            return redirect('employer_profile')
    else:
        c_form = CompanyForm(instance=company)
        p_form = EmployerProfileForm(instance=profile)
        
    return render(request, 'accounts/employer_profile.html', {
        'c_form': c_form,
        'p_form': p_form
    })
