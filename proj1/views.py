
from django.shortcuts import render,redirect
from .import models
from django.http import HttpResponse
from.import emailAPI

import time

#middleware to check session for mainapp routes
def sessioncheck_middleware(get_response):
  def middleware(request):
    if request.path=='/home/' or request.path=='/about/' or request.path=='/contact/' or request.path=='/service/' or request.path=='/login/' or request.path=='/register/':
      request.session['sunm']=None
      request.session['srole']=None
      response = get_response(request)
    else:
      response=get_response(request)
    return response
  return middleware

def home(request):
 return render(request,"home.html")

def about(request):
 return render(request, "about.html")

def contact(request):
 return render(request,"contact.html")
 
def service(request):
 return render(request,"service.html")

def register(request):
 if request.method=="GET":
  return render(request,"register.html",{"output":""})
 else:  
  #receive data from UI
  name=request.POST.get("name")
  email=request.POST.get("email")
  password=request.POST.get("password")
  mobile=request.POST.get("mobile")
  address=request.POST.get("address")
  city=request.POST.get("city")
  gender=request.POST.get("gender")

  #to send verification email
  emailAPI.sendMail(email,password)

  #insert record in database table
  p= models.Register(name=name,email=email,password=password,mobile=mobile,address=address,city=city,gender=gender,status=0,role="user",info=time.asctime())
  
  p.save()

  return render(request,"register.html",{"output":"User Register Successfully..."})

def verify(request):
  vemail=request.GET.get("vemail")
  models.Register.objects.filter(email=vemail).update(status=1)
  return redirect("/login/")

def login(request):
 cunm,cpass="",""
 if request.COOKIES.get("cunm")!=None:
  cunm=request.COOKIES.get("cunm")
  cpass=request.COOKIES.get("cpass")
 print(request.COOKIES.get("cunm"))
 if request.method=="GET":
  return render(request,"login.html",{"cunm":cunm,"cpass":cpass,"Output":""})
 else:
  email=request.POST.get("email")
  password=request.POST.get("password")
  chk=request.POST.get("chk")
  print(chk)  

  userDetails=models.Register.objects.filter(email=email,password=password,status=1)

 if len(userDetails)>0:

   #to store user details is session
   request.session["sunm"]=userDetails[0].name
   request.session["srole"]=userDetails[0].role

   if userDetails[0].role=="admin":
    response= redirect("/myadmin/")
   else:
    response= redirect("/user/")

   #to store cookies in response
   if chk!=None:
    response.set_cookie("cunm",userDetails[0].email,3600)
    response.set_cookie("cpass",userDetails[0].password,3600)

   return response

 else:
  return render(request,"login.html",{"output":"Invalid User or Verify your account","cunm":cunm,"cpass":cpass})

def forget_pw(request):
 if request.method=="GET":
  return render(request,"forget_pw.html",{"Output":""})
 else:
  email=request.POST.get("email")
  password=request.POST.get("password")
  
  #to send verification email
  emailAPI.sendMail(email,password)

'''def pwverify(request):
  vemail=request.GET.get("vemail")
  models.Register.objects.filter(email=vemail)
  return redirect("/changepw/")

def changepw(request):
  if request.method=="GET":
    return render(request,"changepw.html",{"Output":""})
  else:
    return render(request,"changepw.html",{"Output":""})'''
   

def ajaxresponse(request):
  return HttpResponse("<h1>This is AJAX code working</h1>")

def checkEmailAJAX(request):
  email=request.GET.get("email")
  userDetails=models.Register.objects.filter(email__startswith=email)
  flag=0
  if len(userDetails)>0:
    flag=1
  return HttpResponse(flag)