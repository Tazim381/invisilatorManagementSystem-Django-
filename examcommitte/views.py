from ast import Not
from asyncio.windows_events import NULL
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import  teacher,student

# Create your views here.

def home(request):
    return render(request, "authentication/index.html")


def signup(request):
    if request.method == "POST":
        id = request.POST.get('id')
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')

        if len(username) < 3:
            messages.error(request, "Username must be at least 3 charcters!!")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname    
        myuser.save()
        user= teacher()
        user.teacherID = id
        user.userName = username
        user.firstName = fname
        user.lastName = lname
        user.email = email
        user.password =pass1
        user.isCommittee ="False"
        user.isHeadOfCommittee ="False"
        user.save()

        messages.success(request, "Account created successfully")
        return redirect('signin')
    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        if username=="akramkhan" and pass1=="akramkhan":
            teachers = teacher.objects.all()
            teacherobject={'teachers':teachers}
            return render(request,"authentication/chairman.html",teacherobject)
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname': fname})
        else:
            messages.error(request, "Bad credentials")
            return redirect('home')

    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')

def assignStudents(request):
    if request.method=="POST":
        numberofstudents = request.POST['numberofstudent'] 
        year =request.POST['yr'] 
        user =student(year=year,numberOfStudent=numberofstudents)
        user.save()    
    return render(request,"authentication/assignStudents.html")

def createExamCommittee(request):
    teachers=teacher.objects.all()
    teachers={'teachers':teachers}
    if request.method=='POST':
        year=request.POST['yr']
        committee="examcommitte"+year
        user1=User.objects.get(email=request.POST['tea1'])
        user2=User.objects.get(email=request.POST['tea2'])
        user3=User.objects.get(email=request.POST['tea3'])
        teacher1 = teacher.objects.get(email=request.POST['tea1'])
        teacher2 = teacher.objects.get(email=request.POST['tea2'])
        teacher3 = teacher.objects.get(email=request.POST['tea3'])
        teacher1.isCommittee=year
        teacher1.isHeadOfCommittee="True"
        teacher2.isCommittee=year
        teacher3.isCommittee=year
        teacher1.save()
        teacher2.save()
        teacher3.save()
       
        ob=Group.objects.get(name=committee)
        ob.user_set.add(user1)
        ob.user_set.add(user2)
        ob.user_set.add(user3)
    
    return render(request,"authentication/createExamCommittee.html",teachers)

def showExamCommitteeHome(request):
    return render(request,"authentication/showExamCommitteeHome.html")
def showExamCommittee1(request):
    examcommittee=teacher.objects.filter(isCommittee=1)
    examcommittee1={'examcommittee':examcommittee}
    return render(request,"authentication/showExamCommittee.html",examcommittee1)
def showExamCommittee2(request):
    examcommittee=teacher.objects.filter(isCommittee=2)
    examcommittee2={'examcommittee':examcommittee}
    return render(request,"authentication/showExamCommittee.html",examcommittee2)
def showExamCommittee3(request):
    examcommittee=teacher.objects.filter(isCommittee=3)
    examcommittee3={'examcommittee':examcommittee}
    return render(request,"authentication/showExamCommittee.html",examcommittee3)
def showExamCommittee4(request):
    examcommittee=teacher.objects.filter(isCommittee=4)
    examcommittee4={'examcommittee':examcommittee}
    return render(request,"authentication/showExamCommittee.html",examcommittee4)
def showExamCommittee5(request):
    examcommittee=teacher.objects.filter(isCommittee=5)
    examcommittee5={'examcommittee':examcommittee}
    return render(request,"authentication/showExamCommittee.html",examcommittee5)