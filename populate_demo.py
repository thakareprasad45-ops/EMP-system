import os
import django
import sys
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ems_pro.settings')
django.setup()

from accounts.models import User, EmployeeProfile, EmployerProfile, Company
from jobs.models import Job, Application

def create_dummy_data():
    print("Clearing database...")
    User.objects.all().delete()
    Company.objects.all().delete()
    Job.objects.all().delete()
    
    print("Creating admin...")
    admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    
    print("Creating companies and employers...")
    # Company 1
    c1 = Company.objects.create(
        name="TechCorp Solutions",
        email="contact@techcorp.com",
        industry="Software",
        location="New York, NY",
        description="A leading software development company."
    )
    e1 = User.objects.create_user('employer1', 'emp1@example.com', 'emp123', is_employer=True, first_name="John", last_name="Boss")
    EmployerProfile.objects.create(user=e1, company=c1, designation="CEO")
    
    # Company 2
    c2 = Company.objects.create(
        name="Global Finance Inc",
        email="hr@globalfinance.com",
        industry="Finance",
        location="London, UK",
        description="We manage global assets."
    )
    e2 = User.objects.create_user('employer2', 'emp2@example.com', 'emp123', is_employer=True, first_name="Jane", last_name="Smith")
    EmployerProfile.objects.create(user=e2, company=c2, designation="HR Manager")

    print("Creating employees...")
    ee1 = User.objects.create_user('employee1', 'ee1@example.com', 'ee123', is_employee=True, first_name="Alice", last_name="Code")
    EmployeeProfile.objects.create(
        user=ee1, 
        city="New York, NY", 
        skills="Python, Django, JavaScript",
        education="B.Sc Computer Science",
        experience="2 years backend dev"
    )

    ee2 = User.objects.create_user('employee2', 'ee2@example.com', 'ee123', is_employee=True, first_name="Bob", last_name="Data")
    EmployeeProfile.objects.create(
        user=ee2, 
        city="London, UK", 
        skills="SQL, Python, Excel",
        education="B.A Finance",
        experience="1 year analyst"
    )

    print("Creating jobs...")
    j1 = Job.objects.create(
        company=c1,
        title="Django Developer",
        description="We need a strong Django backend dev.",
        requirements="Python, Django, SQL.",
        responsibilities="Build APIs and fix bugs.",
        skills_required="Django",
        location="Remote",
        employment_type="Full Time",
        experience_required="2+ years",
        salary_range="$80k - $100k",
        application_deadline=date.today() + timedelta(days=30),
        status="Open"
    )

    j2 = Job.objects.create(
        company=c1,
        title="Frontend Intern",
        description="Learn React with us.",
        requirements="Basic JS.",
        responsibilities="Assist UI team.",
        skills_required="HTML, CSS, JS",
        location="New York, NY",
        employment_type="Internship",
        experience_required="0 years",
        salary_range="$20/hr",
        application_deadline=date.today() + timedelta(days=15),
        status="Open"
    )

    j3 = Job.objects.create(
        company=c2,
        title="Financial Analyst",
        description="Analyze global trends.",
        requirements="Finance degree.",
        responsibilities="Create reports.",
        skills_required="Excel, SQL",
        location="London, UK",
        employment_type="Full Time",
        experience_required="3+ years",
        salary_range="£50k - £70k",
        application_deadline=date.today() + timedelta(days=45),
        status="Open"
    )

    print("Creating applications...")
    Application.objects.create(
        applicant=ee1.employee_profile,
        job=j1,
        cover_letter="I love Django!",
        status="Under Review"
    )

    Application.objects.create(
        applicant=ee2.employee_profile,
        job=j3,
        cover_letter="I am great at Excel.",
        status="Shortlisted"
    )

    print("Demo data successfully created!")
    
if __name__ == '__main__':
    create_dummy_data()
