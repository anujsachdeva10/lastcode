from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class ApplicantInfoModel(models.Model):
    # Personal Details
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="applicant")
    profile_pic = models.CharField(max_length = 200 , blank=True, null=True)
    description = models.CharField(default = "", max_length=250, blank=True, null=True)
    full_name = models.CharField(default = "", max_length = 50, blank = True, null=True)
    DOB = models.CharField(default = "",max_length = 20, blank = True, null=True)
    gender = models.CharField(default = "Male", max_length = 10, blank = True, null=True)
    address = models.CharField(default = "", max_length = 200, blank = True, null=True)
    state = models.CharField(default = "", max_length = 20, blank = True, null=True)
    pincode = models.PositiveSmallIntegerField(default = 0, null = True)
    category = models.CharField(default = "", max_length = 20, blank = True, null=True)
    marital_status = models.BooleanField(blank = True, null=True)
    # Contact Details.
    phone_number = models.PositiveSmallIntegerField(default = 0, null = True)
    # Career Details.
    total_experience = models.FloatField(default = 0, null = True)
    skillset = models.CharField(default = "", max_length = 20, blank = True, null=True)
    resume = models.CharField(max_length = 200, blank = True, null=True)

    def __str__(self):
        return self.user.username

# Educational Details of the Applicants.
class ApplicantQualificationModel(models.Model):
    applicant = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "qualification")
    qualification_title = models.CharField(max_length = 50, blank = True)
    marks = models.FloatField(null = True)
    passing_year = models.CharField(max_length = 20, blank = True)
    institute = models.CharField(max_length = 50, blank = False)

# Career Details of the Applicants.
class ApplicantExperienceModel(models.Model):
    applicant = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "experience")
    designation = models.CharField(max_length = 20, blank = True)
    from_date = models.CharField(max_length = 20, blank = True)
    to_date = models.CharField(max_length = 20, blank = True)
    institute = models.CharField(max_length = 50, blank = True)
    details = models.CharField(max_length = 200, blank = True)


class CollegeInfoModel(models.Model):
    # username will be collegename, email and password will be in user.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="college")
    empid = models.PositiveSmallIntegerField(null = True)
    empid_pic = models.CharField(max_length = 200, blank = True , null = True)
    location = models.CharField(max_length = 100, blank = True , null = True)
    website = models.CharField(max_length = 100, blank = True , null = True)
    director_mail = models.CharField(max_length = 30, blank = False , null = True)
    registrar_mail = models.CharField(max_length = 30, blank = False , null = True)
    hod_mail = models.CharField(max_length = 30, blank = False , null = True)

    def __str__(self):
        return self.user.username


class EmployeeInfoModel(models.Model):
    # Personal Details.
    college = models.ForeignKey(CollegeInfoModel, on_delete=models.CASCADE, related_name="employee")
    name = models.CharField(max_length = 250, blank = False)
    DOB = models.CharField(max_length = 15, null = False)
    gender = models.CharField(max_length = 10, blank = False)
    category = models.CharField(default = "", max_length = 20, blank = True)
    status = models.CharField(max_length = 15, blank = True, null = True)
    # COMMENTED FIELDS NOT REQUIRED.
    # address = models.CharField(max_length = 100, blank = True)
    # state = models.CharField(default = "", max_length = 20, blank = True)
    # pincode = models.PositiveSmallIntegerField(default = 0, null = True)
    # marital_status = models.BooleanField(blank = True)
    # Contact Details.
    email = models.CharField(max_length = 30, blank = False)
    phone_number = models.PositiveSmallIntegerField(default = 0, null = True)
    # Desgination Details.
    designation = models.CharField(max_length = 250, blank = False)

    def __str__(self):
        return self.name


class VacanciesInfoModel(models.Model):
    college = models.ForeignKey(CollegeInfoModel, on_delete=models.CASCADE, related_name = "vacancy")
    title = models.CharField(max_length = 100, blank = True)   # This may include Prof. for CG, CS etc.
    type = models.CharField(max_length = 100, blank = True)    # This may include assistant prof, prof, intern etc.
    experience = models.CharField(max_length = 100, blank = True)
    date_of_posting = models.CharField(max_length = 20, blank = True)
    state = models.BooleanField(default = True, blank = True)   # Whehter accepting applicants of not.
    description = models.CharField(max_length = 500, blank = True)
    responsibilities = models.CharField(max_length = 500, blank = True)
    qualifications = models.CharField(max_length = 500, blank = True)
    skills = models.CharField(max_length = 200, blank = True)
    compensation = models.FloatField(null = True)



class VacancyApplicantMapping(models.Model):
    applicant = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "applied_vacancies")
    vacancy = models.ForeignKey(VacanciesInfoModel, on_delete = models.CASCADE, related_name = "existing_applicants")


class RecuitmentCommitteeInfoModel(models.Model):
    first_user = models.ForeignKey(EmployeeInfoModel, on_delete=models.CASCADE, related_name = "first_member")
    second_user = models.ForeignKey(EmployeeInfoModel, on_delete=models.CASCADE, related_name = "second_member")
    third_user = models.ForeignKey(EmployeeInfoModel, on_delete=models.CASCADE, related_name = "third_member")
    fourth_user = models.ForeignKey(EmployeeInfoModel, on_delete=models.CASCADE, related_name = "fourth_member")
    fifth_user = models.ForeignKey(EmployeeInfoModel, on_delete=models.CASCADE, related_name = "fifth_member")
    vacancy = models.ForeignKey(VacanciesInfoModel, on_delete=models.CASCADE, related_name = "committee")


