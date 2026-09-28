from django import forms
from .models import Job, Application, ApplicationNote
from accounts.forms import BootstrapFormMixin

class JobForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('company', 'posted_date')
        widgets = {
            'application_deadline': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'requirements': forms.Textarea(attrs={'rows': 3}),
            'responsibilities': forms.Textarea(attrs={'rows': 3}),
        }

class ApplicationForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Application
        fields = ('resume', 'cover_letter')
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your cover letter here...'}),
        }

class ApplicationStatusForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Application
        fields = ('status', 'employer_notes')
        widgets = {
            'employer_notes': forms.Textarea(attrs={'rows': 2}),
        }

class JobSearchForm(BootstrapFormMixin, forms.Form):
    query = forms.CharField(required=False, label='Search', widget=forms.TextInput(attrs={'placeholder': 'Job title, company, location...'}))
    employment_type = forms.ChoiceField(choices=[('', 'All Types')] + Job.EMPLOYMENT_TYPES, required=False)
