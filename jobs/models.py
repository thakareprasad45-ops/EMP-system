from django.db import models
from accounts.models import Company, EmployeeProfile, User

class Job(models.Model):
    EMPLOYMENT_TYPES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
        ('Remote', 'Remote'),
    ]
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Draft', 'Draft'),
    ]
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    responsibilities = models.TextField()
    skills_required = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPES)
    experience_required = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=100)
    posted_date = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')

    def __str__(self):
        return f"{self.title} at {self.company.name}"

class Application(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Under Review', 'Under Review'),
        ('Shortlisted', 'Shortlisted'),
        ('Interview', 'Interview'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
        ('Withdrawn', 'Withdrawn'),
    ]

    applicant = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(upload_to='application_resumes/')
    cover_letter = models.TextField(blank=True)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Applied')
    employer_notes = models.TextField(blank=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('applicant', 'job')

    def __str__(self):
        return f"{self.applicant.user.username} applied to {self.job.title}"

class ApplicationNote(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='notes')
    note = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note on {self.application} by {self.created_by.username}"
