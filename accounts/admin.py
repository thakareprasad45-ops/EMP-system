from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, EmployeeProfile, EmployerProfile, Company

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_employee', 'is_employer', 'is_staff')
    list_filter = ('is_employee', 'is_employer', 'is_staff', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Roles', {'fields': ('is_employee', 'is_employer')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(EmployeeProfile)
admin.site.register(EmployerProfile)
admin.site.register(Company)
