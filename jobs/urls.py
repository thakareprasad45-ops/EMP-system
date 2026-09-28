from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),
    path('jobs/<int:pk>/apply/', views.apply_job, name='apply_job'),
    
    # Employee
    path('employee/dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('employee/applications/', views.employee_applications, name='employee_applications'),
    
    # Employer
    path('employer/dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('employer/jobs/create/', views.job_create, name='job_create'),
    path('employer/jobs/<int:pk>/edit/', views.job_edit, name='job_edit'),
    path('employer/jobs/<int:pk>/applicants/', views.job_applicants, name='job_applicants'),
    
    # Shared
    path('application/<int:pk>/', views.application_detail, name='application_detail'),
]
