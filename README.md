# EMPLOYMENT MANAGEMENT SYSTEM PRO

## Project Description
Employment Management System Pro (EMS PRO) is a comprehensive web-based platform built with Django. It bridges the gap between job seekers (employees) and companies (employers) by providing a centralized hub for posting job vacancies, tracking applications, and managing profiles. 

## Problem Statement
The modern job market is fragmented. Employers struggle to manage applications across multiple channels, while job seekers find it difficult to track their application statuses and communicate effectively with potential employers.

## Objectives
- Create a streamlined portal for job discovery and application.
- Provide a robust dashboard for employers to manage job postings and applicants.
- Implement an intuitive application tracking system for job seekers.
- Demonstrate standard web development practices and Django framework capabilities.

## Features
- **Role-based Authentication:** Separate portal experiences for Employees, Employers, and Admins.
- **Job seeker Dashboard:** Browse jobs, filter by criteria, apply seamlessly, and track application status.
- **Employer Dashboard:** Post jobs, view incoming applications, review resumes, and update applicant statuses.
- **Profile Management:** Detailed company and candidate profiles.
- **Admin Control:** Absolute oversight of users, jobs, applications, and system metrics.

## Technologies
- **Backend:** Python 3, Django
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite (development)
- **File Handling:** Django Media (Pillow for images, standard FileField for Resumes)

## System Architecture (MVT)
This project follows Django's robust Model-View-Template pattern:
- **Models:** Database tables defined globally (`User`, `Job`, `Application`, etc.).
- **Views:** Python functions managing business logic and authorization.
- **Templates:** HTML files mixed with Django Template Language to render views securely dynamically.

## Installation Instructions

1. Clone or extract the project.
2. Open terminal and navigate to the project root:
   ```bash
   cd employment_system_pro
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install django pillow
   ```
5. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Populate sample data (Optional but recommended):
   ```bash
   python populate_demo.py
   ```
7. Start the server:
   ```bash
   python manage.py runserver
   ```
8. Access the site at `http://127.0.0.1:8000/`

## Demo Accounts (from populate_demo.py)
**Admin:** 
- Username: `admin`
- Password: `admin123`

**Employer 1:**
- Username: `employer1`
- Password: `emp123`

**Employee 1:**
- Username: `employee1`
- Password: `ee123`

## Future Improvements
- Email notifications when application status updates.
- Real-time chat between employer and applicant.
- Advanced AI-based resume parsing.
- Integration with external cloud storage (AWS S3) for resumes.
