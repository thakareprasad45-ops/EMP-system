from django.contrib import admin
from .models import Job, Application, ApplicationNote

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'employment_type', 'status', 'posted_date')
    list_filter = ('status', 'employment_type', 'company')
    search_fields = ('title', 'description', 'company__name')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'job', 'status', 'application_date')
    list_filter = ('status', 'job__company')
    search_fields = ('applicant__user__username', 'job__title')

admin.site.register(ApplicationNote)
