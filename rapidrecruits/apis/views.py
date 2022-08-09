from django.shortcuts import render
from apis.models import ApplicantExperienceModel, ApplicantInfoModel
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate, logout
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class ApplicantAPIView(APIView):

    def get(self, request, username, format = None):
        # if (pk == None):
        #     applicants = ApplicantInfoModel.objects.all()
        #     result = []
        #     for applicant in applicants:
        #         temp_result = {}
        #         temp_result["id"] = 
        #         temp_result["username"] = applicant.user.username
        #         temp_result["email"] = applicant.user.email
        #         temp_result["description"] = applicant.description
        #         temp_result["full_name"] = applicant.full_name
        #         temp_result["DOB"] = applicant.DOB
        #         temp_result["gender"] = applicant.gender
        #         temp_result["address"] = applicant.address
        #         temp_result["state"] = applicant.state
        #         temp_result["pincode"] = applicant.pincode
        #         temp_result["category"] = applicant.category
        #         temp_result["marital_status"] = applicant.marital_status
        #         temp_result["phone_number"] = applicant.phone_number
        #         temp_result["total_experience"] = applicant.total_experience
        #         temp_result["skillset"] = applicant.skillset
        #         result.append(temp_result)
        #     return Response(result, status = 200)

        # else:
        user = User.objects.get(username = username)
        applicant = ApplicantInfoModel.objects.get(user = user)
        temp_result = {}
        temp_result["username"] = applicant.user.username
        temp_result["email"] = applicant.user.email
        temp_result["description"] = applicant.description
        temp_result["full_name"] = applicant.full_name
        temp_result["DOB"] = applicant.DOB
        temp_result["gender"] = applicant.gender
        temp_result["address"] = applicant.address
        temp_result["state"] = applicant.state
        temp_result["pincode"] = applicant.pincode
        temp_result["category"] = applicant.category
        temp_result["marital_status"] = applicant.marital_status
        temp_result["phone_number"] = applicant.phone_number
        temp_result["total_experience"] = applicant.total_experience
        temp_result["skillset"] = applicant.skillset
        return Response(temp_result, status = 200)


    def post(self, request, format = None):
        if (request.data["purpose"] == "signup"):
            username = request.data["username"]
            email = request.data["email"]
            password = request.data["password"]
            confirm_password = request.data["confirm_password"]
            if (password == confirm_password):
                user = User.objects.create(username = username, email = email, password = password)
                user.set_password(user.password)
                user.save()
                login(request, user)
            return Response({"mssg": "user signed up successfully!"}, status = 200)
        elif (request.data["purpose"] == "login"):
            if (authenticate(username = request.data["username"], password = request.data["password"])):
                return Response({"mssg": "user logedin successfully!"}, status = 200)
            else:
                return Response({"mssg": "login failed!"}, status = 400)
        elif (request.data["purpose"] == "fill details"):
            user = User.objects.get(username = request.data["username"])
            request.data["details"]["user"] = user
            ApplicantInfoModel.objects.create(**request.data["details"])
            return Response({"mssg": "data updated successfully!"}, status = 202)


    def put(self, request, username, format = None):
        user = User.objects.get(username = username)
        applicant = ApplicantInfoModel.objects.get(user = user)
        user.email = request.data.get("email")
        applicant.description = request.data.get("description")
        applicant.full_name = request.data.get("full_name")
        applicant.DOB = request.data.get("DOB")
        applicant.gender = request.data.get("gender")
        applicant.address = request.data.get("address")
        applicant.state = request.data.get("state")
        applicant.pincode = request.data.get("pincode")
        applicant.category = request.data.get("category")
        applicant.marital_status = request.data.get("marital_status")
        applicant.phone_number = request.data.get("phone_number")
        applicant.total_experience = request.data.get("total_experience")
        applicant.skillset = request.data.get("skillset")
        user.save()
        applicant.save()
        return Response({"mssg" : "user updated successfully"}, status = 204)

    def delete(self, request, username, format = None):
        user = User.objects.get(username = username)
        applicant = ApplicantInfoModel.objects.get(user = user)
        user.delete()
        applicant.delete()
        return Response({"mssg": "user delete successfully"}, status = 200)
