from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    phone = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    education = models.TextField(blank=True, help_text="List your educational background")
    experience = models.TextField(blank=True, help_text="List your work experience")
    skills = models.CharField(max_length=255, blank=True, help_text="Comma separated skills")
    current_job_title = models.CharField(max_length=100, blank=True)
    expected_salary = models.CharField(max_length=100, blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Company(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    industry = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    number_of_employees = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile')
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='employer', null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    designation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username} - Employer"
