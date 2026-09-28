from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/employee/', views.register_employee, name='register_employee'),
    path('register/employer/', views.register_employer, name='register_employer'),
    path('profile/employee/', views.employee_profile, name='employee_profile'),
    path('profile/employer/', views.employer_profile, name='employer_profile'),
]
