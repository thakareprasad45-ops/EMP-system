# VIVA CHEAT SHEET

*(Memorize these short answers!)*

**Q1: What is Django?**
A: A Python-based web framework that allows for rapid development and clean design.

**Q2: Why use Django instead of Flask?**
A: Django is "batteries-included." It comes with built-in authentication, ORM, and an Admin panel, whereas Flask requires you to build or install those manually.

**Q3: What is MVT architecture?**
A: Model (database structure), View (business logic), Template (HTML layout).

**Q4: What is Django ORM?**
A: Object-Relational Mapper. It lets us interact with the database using Python code instead of writing raw SQL.

**Q5: What is a Model?**
A: A Python class that defines the structure of a database table. (e.g., our `Job` or `Application` models).

**Q6: What is a View?**
A: A Python function that takes a web request and returns a web response (like an HTML page or an error).

**Q7: What is a Template?**
A: An HTML file containing Django tags `{% %}` that allow us to display dynamic data from the View.

**Q8: What is a migration?**
A: A file that contains instructions to update the database schema (tables) based on changes made to our models.

**Q9: What is CRUD?**
A: Create, Read, Update, Delete. Our project does all four (e.g., Create a job, Read applicants, Update status, Delete jobs in admin).

**Q10: What is a ForeignKey?**
A: A database link that creates a Many-to-One relationship. (Many Jobs belong to One Company).

**Q11: What is a OneToOneField?**
A: A link creating a strict 1-to-1 relationship. (One User has exactly One EmployeeProfile).

**Q12: Why use SQLite?**
A: It is a lightweight database stored in a single file, perfect for development. In production, we'd swap it for PostgreSQL.

**Q13: How does authentication work?**
A: Django handles the hashing of passwords and creates session cookies to remember users once they log in safely.

**Q14: Authentication vs Authorization?**
A: Authentication is "Who are you?" (login). Authorization is "What are you allowed to do?" (e.g., only employers can post jobs).

**Q15: How are passwords stored?**
A: Django securely hashes them (using algorithms like PBKDF2); they are never stored as plain text.

**Q16: What is CSRF?**
A: Cross-Site Request Forgery. Django uses `{% csrf_token %}` to ensure form submissions actually come from our website, not a hacker's site.

**Q17: How does file upload work?**
A: We configure `MEDIA_ROOT` and `MEDIA_URL` in settings. Forms use `enctype="multipart/form-data"` to send the file to the server.

**Q18: How do you prevent duplicate applications?**
A: In the `Application` model, we used `unique_together = ('applicant', 'job')`. The database will reject a second application.

**Q19: How do you prevent employers from modifying other employers' jobs?**
A: In our `job_edit` view, we query: `get_object_or_404(Job, pk=pk, company=request.user.employer_profile.company)`. It fails if it's not their company.

**Q20: What is a QuerySet?**
A: A list of objects retrieved from the database. E.g., `Job.objects.filter(status='Open')` returns a QuerySet of open jobs.

**Q21: What is a ModelForm?**
A: A Django feature that automatically generates an HTML form straight from a Model, saving us from writing repetitive HTML inputs.

**Q22: How does Django communicate with the database?**
A: Through the ORM engine specified in the `DATABASES` setting (SQLite in our case).

**Q23: How would you deploy this application?**
A: By configuring a service like Gunicorn for the web server, Nginx for static files, a PostgreSQL database, and hosting it on a platform like Render or AWS.

**Q24: What happens if a Company is deleted?**
A: Because we used `on_delete=models.CASCADE` on the ForeignKey, all Jobs associated with that company will also be deleted automatically to prevent orphaned data.

**Q25: What is the Django Admin Panel?**
A: A built-in, secure interface that reads our models and provides a fully functional dashboard to manage database records without writing code.
