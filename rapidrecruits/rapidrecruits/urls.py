"""rapidrecruits URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/applicant/', views.ApplicantAPIView.as_view(), name = "applicant"),
    path('api/applicant/<str:username>/', views.ApplicantAPIView.as_view()),
    path('api/college/', views.CollegeAPIView.as_view(), name="college"),
    path('api/college/<str:username>/', views.CollegeAPIView.as_view()),
    path('api/qualification/<str:username>/', views.QualificationAPIView.as_view()),
    path('api/experience/<str:username>/', views.ExperienceAPIView.as_view()),
    path('api/employee/<str:college_name>/', views.EmployeeAPIView.as_view()),
    path('api/get_employee_by_id/<str:college_name>/<int:id>/', views.get_employee_by_id),
    path('api/changestatus/<str:college_name>/<int:id>/', views.Change_employee_status),
    path('api/vacancies/<str:college_name>/', views.VacanciesAPIView.as_view()),
    path('api/vacancies/', views.VacanciesAPIView.as_view()),
    path('api/getuservacancies/<str:username>/', views.get_vacancies_for_applicant),
    path('api/getvacancyapplicants/<int:id>/', views.get_applicants_for_vacancy),
    path('api/applyvacancy/<str:username>/', views.apply_for_vacancy),
]
