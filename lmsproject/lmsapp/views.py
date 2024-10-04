from django.shortcuts import render,redirect,reverse
from . models import Enquiry,Student,Login
from datetime import date
from django.contrib import messages
from adminapp.models import Program,Branch,Year

# Create your views here.
def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,"aboutus.html")

def registraton(request):
    if request.method=='POST':
        rollno=request.POST['rollno']
        name=request.POST['name']
        fname=request.POST['fname']
        mname=request.POST['mname']
        gender=request.POST['gender']
        address=request.POST['address']
        contactno=request.POST['contactno']
        program=request.POST['program']
        branch=request.POST['branch']
        year=request.POST['year']
        emailaddress=request.POST['emailaddress']
        password=request.POST['password']
        regdate=date.today()
        usertype='student'
        status='false'
        stu=Student(rollno=rollno,name=name,fname=fname,mname=mname,gender=gender,branch=branch,address=address,program=program,year=year,contactno=contactno,emailaddress=emailaddress,regdate=regdate)
        log=Login(userid=rollno,password=password,status=status,usertype=usertype)
        stu.save()
        log.save()
        messages.success(request,'student registration is done')
    program=Program.objects.all()
    branch=Branch.objects.all()
    year=Year.objects.all()
    return render(request,"registration.html",locals())

def login(request):
    if request.method=="POST":
        userid=request.POST['userid']
        password=request.POST['password']
        
        try:
            obj=Login.objects.get(userid=userid,password=password)
            if obj.usertype=="student":
                request.session['rollno']=userid
                return redirect(reverse('studentapp:studenthome'))
            elif obj.usertype=="admin":
                request.session['adminid']=userid
                return redirect (reverse('adminapp:adminhome'))
        except:
            messages.success(request,'invalid user')
    return render(request,"login.html")

def contactus(request):
    if request.method=="POST":
        name=request.POST['name']
        gender=request.POST['gender']
        address=request.POST['address']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        enquirytext=request.POST['enquirytext']
        enquirydate=date.today()
        enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
        enq.save()
        messages.success(request,'your enquiry is submitted')

    
       

                                
    return render(request,"contactus.html")

