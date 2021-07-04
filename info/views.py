from django.http import response
from django.shortcuts import render
from .models import  Register
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):

    if request.method=='POST':
        name=request.POST["name"]
        mob=request.POST["mob"]
        email=request.POST["email"]
        branch=request.POST["branch"]
        password=request.POST["password"]
      
        x=Register.objects.create(name=name,email=email,mob=mob,branch=branch,password=password)
        x.save()
        messages.success(request, "Registration Successfull")
       
        return render(request,'index.html')

    return render(request,'index.html')