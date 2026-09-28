from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job, Application
from .forms import JobForm, ApplicationForm, ApplicationStatusForm, JobSearchForm
from django.db.models import Q

def home(request):
    recent_jobs = Job.objects.filter(status='Open').order_by('-posted_date')[:5]
    return render(request, 'jobs/home.html', {'recent_jobs': recent_jobs})

def job_list(request):
    jobs = Job.objects.filter(status='Open').order_by('-posted_date')
    form = JobSearchForm(request.GET)
    
    if form.is_valid():
        query = form.cleaned_data.get('query')
        emp_type = form.cleaned_data.get('employment_type')
        if query:
            jobs = jobs.filter(Q(title__icontains=query) | Q(company__name__icontains=query) | Q(location__icontains=query))
        if emp_type:
            jobs = jobs.filter(employment_type=emp_type)
            
    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'form': form})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    has_applied = False
    if request.user.is_authenticated and request.user.is_employee:
        has_applied = Application.objects.filter(job=job, applicant=request.user.employee_profile).exists()
    
    return render(request, 'jobs/job_detail.html', {'job': job, 'has_applied': has_applied})

@login_required
def apply_job(request, pk):
    if not request.user.is_employee:
        messages.error(request, "Only employees can apply for jobs.")
        return redirect('job_detail', pk=pk)
        
    job = get_object_or_404(Job, pk=pk)
    profile = request.user.employee_profile
    
    if Application.objects.filter(job=job, applicant=profile).exists():
        messages.warning(request, "You have already applied for this job.")
        return redirect('employee_applications')
        
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = profile
            application.save()
            messages.success(request, f"Successfully applied for {job.title}!")
            return redirect('employee_applications')
    else:
        # Pre-fill resume if available
        initial = {}
        if profile.resume:
            initial['resume'] = profile.resume
        form = ApplicationForm(initial=initial)
        
    return render(request, 'jobs/apply_job.html', {'form': form, 'job': job})

@login_required
def employee_dashboard(request):
    if not request.user.is_employee:
        return redirect('home')
    apps = Application.objects.filter(applicant=request.user.employee_profile)
    stats = {
        'total': apps.count(),
        'pending': apps.filter(status='Applied').count() + apps.filter(status='Under Review').count(),
        'shortlisted': apps.filter(status='Shortlisted').count(),
        'interview': apps.filter(status='Interview').count(),
        'selected': apps.filter(status='Selected').count(),
        'rejected': apps.filter(status='Rejected').count(),
    }
    return render(request, 'jobs/employee_dashboard.html', {'stats': stats, 'recent_apps': apps.order_by('-application_date')[:5]})

@login_required
def employee_applications(request):
    if not request.user.is_employee:
        return redirect('home')
    apps = Application.objects.filter(applicant=request.user.employee_profile).order_by('-application_date')
    return render(request, 'jobs/employee_applications.html', {'apps': apps})

@login_required
def employer_dashboard(request):
    if not request.user.is_employer:
        return redirect('home')
    company = request.user.employer_profile.company
    if not company:
        messages.warning(request, "Please set up your company profile first.")
        return redirect('employer_profile')
        
    jobs = Job.objects.filter(company=company)
    apps = Application.objects.filter(job__company=company)
    
    stats = {
        'total_jobs': jobs.count(),
        'active_jobs': jobs.filter(status='Open').count(),
        'total_applicants': apps.count(),
        'under_review': apps.filter(status='Under Review').count(),
        'shortlisted': apps.filter(status='Shortlisted').count(),
        'selected': apps.filter(status='Selected').count(),
    }
    return render(request, 'jobs/employer_dashboard.html', {'stats': stats, 'recent_apps': apps.order_by('-application_date')[:5]})

@login_required
def job_create(request):
    if not request.user.is_employer:
        return redirect('home')
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user.employer_profile.company
            job.save()
            messages.success(request, "Job posted successfully!")
            return redirect('employer_dashboard')
    else:
        form = JobForm()
    return render(request, 'jobs/job_form.html', {'form': form, 'title': 'Post a Job'})

@login_required
def job_edit(request, pk):
    job = get_object_or_404(Job, pk=pk, company=request.user.employer_profile.company)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "Job updated successfully!")
            return redirect('employer_dashboard')
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/job_form.html', {'form': form, 'title': 'Edit Job'})

@login_required
def job_applicants(request, pk):
    job = get_object_or_404(Job, pk=pk, company=request.user.employer_profile.company)
    applications = job.applications.all()
    return render(request, 'jobs/job_applicants.html', {'job': job, 'applications': applications})

@login_required
def application_detail(request, pk):
    app = get_object_or_404(Application, pk=pk)
    
    # Permission check
    is_employee = request.user.is_employee and app.applicant.user == request.user
    is_employer = request.user.is_employer and app.job.company == request.user.employer_profile.company
    
    if not (is_employee or is_employer):
        messages.error(request, "You do not have permission to view this application.")
        return redirect('home')
        
    form = None
    if is_employer:
        if request.method == 'POST':
            form = ApplicationStatusForm(request.POST, instance=app)
            if form.is_valid():
                form.save()
                messages.success(request, "Application status updated!")
                return redirect('application_detail', pk=pk)
        else:
            form = ApplicationStatusForm(instance=app)
            
    return render(request, 'jobs/application_detail.html', {'app': app, 'form': form, 'is_employer': is_employer})
