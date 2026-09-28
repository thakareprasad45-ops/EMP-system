from django import forms
from django.contrib.auth.forms import UserCreationForm

class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if not getattr(self.fields[field].widget, 'input_type', None) in ['checkbox', 'radio']:
                self.fields[field].widget.attrs['class'] = 'form-control mb-3'

from .models import User, EmployeeProfile, EmployerProfile, Company

class EmployeeSignUpForm(BootstrapFormMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employee = True
        if commit:
            user.save()
            EmployeeProfile.objects.create(user=user)
        return user

class EmployerSignUpForm(BootstrapFormMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employer = True
        if commit:
            user.save()
            company = Company.objects.create(name=f"{user.username}'s Company")
            EmployerProfile.objects.create(user=user, company=company)
        return user

class EmployeeProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        exclude = ('user',)
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'about': forms.Textarea(attrs={'rows': 3}),
            'education': forms.Textarea(attrs={'rows': 3}),
            'experience': forms.Textarea(attrs={'rows': 3}),
        }

class CompanyForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class EmployerProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ('phone', 'designation')
