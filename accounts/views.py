from django.shortcuts import render
from django.http import HttpResponse
from .models import user_data
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def register(request):
    if request.method=="POST":
        first_name=request.POST['firstName']
        middle_name=request.POST['middleName']
        last_name=request.POST['lastName']
        email=request.POST['email']
        password=request.POST['password']
        confirmPassword=request.POST['confirmPassword']
        phone=request.POST['phone']
        gender=request.POST['gender']
        salary=request.POST['salary']
        address=request.POST['address']
        is_exist=User.objects.filter(email=email).exists()
        if not is_exist:
            return HttpResponse("Ori babu already unnad ra nayana ")
        else:
            print(middle_name,last_name,email,password,confirmPassword,phone,gender,salary,address)
            user=user_data(first_name=first_name,middle_name=middle_name,last_name=last_name,email=email,password=password,phn_no=phone,gender=gender,salary=salary,address=address)
            user.save()
            msg="OK data theeskunta kangaru padaku {}".format(first_name)
            return HttpResponse(msg)
    else:
        return render(request,'register.html')
def login(request):
    if request.method=="POST":
        email= request.POST["email"]
        password= request.POST["password"]
        user1=authenticate(request,email=email,password=password)
        print(email,password)
        if user1 is not None:
            print(user1)
            return HttpResponse("Ahhh unnav le ")
        else:
            print(user1)
            return HttpResponse("chal mingeyu")
    else:
        return render(request,"login.html")