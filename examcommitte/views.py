from ast import Not
from asyncio.windows_events import NULL
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import  teacher,student,course,createdExamCommittee,Semister,routine,teacherCount
from django.db.models import Q

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
        user.isCommittee = 0
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
            headOfCommittee1= teacher.objects.get(Q(isCommittee='1')& Q(isHeadOfCommittee="True"))
            print(headOfCommittee1.firstName)
            teachers = teacher.objects.get(userName = username)
            print(teachers.firstName)
            if(str(headOfCommittee1.firstName)==str(teachers.firstName)):
                courses= course.objects.all()
                return render(request,"authentication/examCommittee1.html",{'headOfCommittee1':headOfCommittee1})
            
            headOfCommittee2= teacher.objects.get(Q(isCommittee='2')& Q(isHeadOfCommittee="True"))
            print(headOfCommittee2.firstName)
            teachers = teacher.objects.get(userName = username)
            print(teachers.firstName)
            if(str(headOfCommittee2.firstName)==str(teachers.firstName)):
                courses= course.objects.all()
                return render(request,"authentication/examCommittee2.html",{'headOfCommittee2':headOfCommittee2})
            
            headOfCommittee3= teacher.objects.get(Q(isCommittee='3')& Q(isHeadOfCommittee="True"))
            print(headOfCommittee3.firstName)
            teachers = teacher.objects.get(userName = username)
            print(teachers.firstName)
            if(str(headOfCommittee3.firstName)==str(teachers.firstName)):
                courses= course.objects.all()
                return render(request,"authentication/examCommittee3.html",{'headOfCommittee3':headOfCommittee3})
            
            headOfCommittee4= teacher.objects.get(Q(isCommittee='4')& Q(isHeadOfCommittee="True"))
            print(headOfCommittee4.firstName)
            teachers = teacher.objects.get(userName = username)
            print(teachers.firstName)
            if(str(headOfCommittee4.firstName)==str(teachers.firstName)):
                courses= course.objects.all()
                return render(request,"authentication/examCommittee4.html",{'headOfCommittee4':headOfCommittee4})
            
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname': fname})
        else:
            messages.error(request, "Bad credentials")
            

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
        if(int(teacher1.isCommittee) | int(teacher2.isCommittee) | int(teacher3.isCommittee)):
            messages.error(request, "Teacher is already in another committee. Please try another teacher")
            return redirect('createexamcommittee')
        if(teacher.objects.filter(isCommittee = year).exists()):
            messages.error(request, "Exam Committee is already created . Please create another exam committee")
            return redirect('createexamcommittee')
        createCommittee = createdExamCommittee()
        if year == "1":
            createCommittee.examCommitteeYear ="First Year"
            createCommittee. examCommitteeStatus="Created"
        if year == "2":
            createCommittee.examCommitteeYear ="Second Year"
            createCommittee. examCommitteeStatus="Created"
        if year == "3":
            createCommittee.examCommitteeYear ="Third Year"
            createCommittee. examCommitteeStatus="Created"
        if year == "4":
            createCommittee.examCommitteeYear ="Fourth Year"
            createCommittee. examCommitteeStatus="Created"
        createCommittee.save()
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


def teachersList(request):
    teachers = teacher.objects.all()
    teachers ={'teachers':teachers}
    return render(request,"authentication/showTeachersList.html",teachers)


def createCourse(request):
    teachers = teacher.objects.all()
    teachers ={'teachers':teachers}
    if request.method == "POST":
        courseCode = request.POST.get('courseCode')
        courseTitle = request.POST.get('courseTitle')
        courseCredit = request.POST.get('courseCredit')
        courseTeacher = request.POST.get('courseTeacher')
        externalTeacher = request.POST.get('externalTeacher')
       
        if(course.objects.filter(courseCode =courseCode).exists()):
            messages.error(request, "Course already created. Please Try another")
            return redirect('createCourse')
       
        courses = course()
        courses.courseCode = courseCode
        courses.courseTitle = courseTitle
        courses.courseCredit = courseCredit
        courses.courseTeacher = courseTeacher
        courses.externalTeacher = externalTeacher
        courses.save()
        messages.success(request, "sussessfully created course")
    return render(request,"authentication/createCourse.html",teachers)


def createdexamcommittee(request):
    createdCommittee =  createdExamCommittee.objects.all()
    createdCommittee = {'createdCommittee':createdCommittee}
    return render(request,"authentication/createdExamCommittee.html",createdCommittee)


def createRoutine1(request):
    courses = course.objects.filter(courseCode__gte ='100',courseCode__lte = '199')
    courses={'courses':courses}
    if request.method=='POST':
        if(request.POST['semister']!='1'):
            messages.success(request,"Sorry You Only Create Routine For First Year Students")
            return render(request,"authentication/createRoutine1.html")
        ready = routine.objects.all()
        for subjects in ready:
            print(subjects) 
            subject = course.objects.get(courseCode=request.POST['course'])
            print (subject.courseTitle +"HO")
            if str(subjects) == str(subject.courseTitle):
                messages.error(request, "Routine Already Created for this Course")
                return render(request,"authentication/createRoutine1.html")
            
        Courses=course.objects.get(courseCode=request.POST['course'])
        date=request.POST['date']
        start=request.POST['start']
        end=request.POST['end']
        students=student.objects.get(year=request.POST['semister'])
        semister=Semister(semNo=request.POST['semister'])
        routines=routine(courseCode=Courses,date=date,start=start,end=end)
        routines.semester= semister
        routines.save()
        response='/createRoutine11/'+str(Courses.courseCode)+'/'+str(students.numberOfStudent)
        return redirect(response)
    return render(request,"authentication/createRoutine1.html",courses)

def createRoutine11(request,id,id2):
    id2=int(id2)
    eb= teacher.objects.all()
    cont={
        'ob':range(int(id2/12)),
        'eb':eb
    }
    if request.method=='POST':
        co=course.objects.get(courseCode=int(id))
        for o in range(int(id2/12)):
            st="so"+str(o)
            oo=teacher.objects.get(userName=request.POST.get(st))
            rou=routine.objects.get(courseCode=co)
            rou.teachers.add(oo)
           
            if(teacherCount.objects.filter(firstName = oo.firstName).exists()):
                 count = teacherCount.objects.get(firstName = oo.firstName)
                 count.count = count.count+1
            else:  
                count = teacherCount() 
                count.firstName = oo.firstName
                count.lastName = oo.lastName
                count.count = count.count+1
            count.save()
        rou=routine.objects.filter(courseCode=co)
        response='/'
        return render(request,'authentication/showRoutine1.html')
    
    return render(request,'authentication/createRoutine11.html',cont)

def showRoutine1(request):
    routines = routine.objects.filter(semester="1")
    for routin in routines:
        for teacher in routin.teachers.all():
            print(teacher)
    return render(request,'authentication/showRoutine1.html',{'routines':routines})


def createRoutine2(request):
    courses = course.objects.filter(courseCode__gte ='200',courseCode__lte = '299')
    courses={'courses':courses}
    if request.method=='POST':
        if(request.POST['semister']!='2'):
            messages.success(request,"Sorry You Only Create Routine For 2nd Year Students")
            return render(request,"authentication/createRoutine2.html")
        ready = routine.objects.all()
        for subjects in ready:
            print(subjects) 
            subject = course.objects.get(courseCode=request.POST['course'])
            print (subject.courseTitle +"HO")
            if str(subjects) == str(subject.courseTitle):
                messages.error(request, "Routine Already Created for this Course")
                return render(request,"authentication/createRoutine2.html")
            
        Courses=course.objects.get(courseCode=request.POST['course'])
        date=request.POST['date']
        start=request.POST['start']
        end=request.POST['end']
        students=student.objects.get(year=request.POST['semister'])
        semister=Semister(semNo=request.POST['semister'])
        routines=routine(courseCode=Courses,date=date,start=start,end=end)
        routines.semester= semister
        routines.save()
        response='/createRoutine22/'+str(Courses.courseCode)+'/'+str(students.numberOfStudent)
        return redirect(response)
    return render(request,"authentication/createRoutine2.html",courses)


def createRoutine22(request,id,id2):
    id2=int(id2)
    eb= teacher.objects.all()
    cont={
        'ob':range(int(id2/12)),
        'eb':eb
    }
    if request.method=='POST':
        co=course.objects.get(courseCode=int(id))
        for o in range(int(id2/12)):
            st="so"+str(o)
            oo=teacher.objects.get(userName=request.POST.get(st))
            rou=routine.objects.get(courseCode=co)
            rou.teachers.add(oo)
           
            if(teacherCount.objects.filter(firstName = oo.firstName).exists()):
                 count = teacherCount.objects.get(firstName = oo.firstName)
                 count.count = count.count+1
            else:  
                count = teacherCount() 
                count.firstName = oo.firstName
                count.lastName = oo.lastName
                count.count = count.count+1
            count.save()
        rou=routine.objects.filter(courseCode=co)
        response='/'
        return render(request,'authentication/showRoutine2.html')
    
    return render(request,'authentication/createRoutine22.html',cont)


def showRoutine2(request):
    routines = routine.objects.filter(semester="2")
    for routin in routines:
        for teacher in routin.teachers.all():
            print(teacher)
    return render(request,'authentication/showRoutine2.html',{'routines':routines})


def createRoutine3(request):
    courses = course.objects.filter(courseCode__gte ='300',courseCode__lte = '399')
    courses={'courses':courses}
    if request.method=='POST':
        if(request.POST['semister']!='3'):
            messages.success(request,"Sorry You Only Create Routine For 3rd Year Students")
            return render(request,"authentication/createRoutine3.html")
        ready = routine.objects.all()
        for subjects in ready:
            print(subjects) 
            subject = course.objects.get(courseCode=request.POST['course'])
            print (subject.courseTitle +"HO")
            if str(subjects) == str(subject.courseTitle):
                messages.error(request, "Routine Already Created for this Course")
                return render(request,"authentication/createRoutine3.html")
            
        Courses=course.objects.get(courseCode=request.POST['course'])
        date=request.POST['date']
        start=request.POST['start']
        end=request.POST['end']
        students=student.objects.get(year=request.POST['semister'])
        semister=Semister(semNo=request.POST['semister'])
        routines=routine(courseCode=Courses,date=date,start=start,end=end)
        routines.semester= semister
        routines.save()
        response='/createRoutine33/'+str(Courses.courseCode)+'/'+str(students.numberOfStudent)
        return redirect(response)
    return render(request,"authentication/createRoutine3.html",courses)


def createRoutine33(request,id,id2):
    id2=int(id2)
    eb= teacher.objects.all()
    cont={
        'ob':range(int(id2/12)),
        'eb':eb
    }
    if request.method=='POST':
        co=course.objects.get(courseCode=int(id))
        for o in range(int(id2/12)):
            st="so"+str(o)
            oo=teacher.objects.get(userName=request.POST.get(st))
            rou=routine.objects.get(courseCode=co)
            rou.teachers.add(oo)
           
            if(teacherCount.objects.filter(firstName = oo.firstName).exists()):
                 count = teacherCount.objects.get(firstName = oo.firstName)
                 count.count = count.count+1
            else:  
                count = teacherCount() 
                count.firstName = oo.firstName
                count.lastName = oo.lastName
                count.count = count.count+1
            count.save()
        rou=routine.objects.filter(courseCode=co)
        response='/'
        return render(request,'authentication/showRoutine3.html')
    
    return render(request,'authentication/createRoutine33.html',cont)


def showRoutine3(request):
    routines = routine.objects.filter(semester="3")
    for routin in routines:
        for teacher in routin.teachers.all():
            print(teacher)
    return render(request,'authentication/showRoutine3.html',{'routines':routines})


def createRoutine4(request):
    courses = course.objects.filter(courseCode__gte ='400',courseCode__lte = '499')
    courses={'courses':courses}
    if request.method=='POST':
        if(request.POST['semister']!='4'):
            messages.success(request,"Sorry You Only Create Routine For 4th Year Students")
            return render(request,"authentication/createRoutine4.html")
        ready = routine.objects.all()
        for subjects in ready:
            print(subjects) 
            subject = course.objects.get(courseCode=request.POST['course'])
            print (subject.courseTitle +"HO")
            if str(subjects) == str(subject.courseTitle):
                messages.error(request, "Routine Already Created for this Course")
                return render(request,"authentication/createRoutine4.html")
            
        Courses=course.objects.get(courseCode=request.POST['course'])
        date=request.POST['date']
        start=request.POST['start']
        end=request.POST['end']
        students=student.objects.get(year=request.POST['semister'])
        semister=Semister(semNo=request.POST['semister'])
        routines=routine(courseCode=Courses,date=date,start=start,end=end)
        routines.semester= semister
        routines.save()
        response='/createRoutine44/'+str(Courses.courseCode)+'/'+str(students.numberOfStudent)
        return redirect(response)
    return render(request,"authentication/createRoutine4.html",courses)


def createRoutine44(request,id,id2):
    id2=int(id2)
    eb= teacher.objects.all()
    cont={
        'ob':range(int(id2/12)),
        'eb':eb
    }
    if request.method=='POST':
        co=course.objects.get(courseCode=int(id))
        for o in range(int(id2/12)):
            st="so"+str(o)
            oo=teacher.objects.get(userName=request.POST.get(st))
            rou=routine.objects.get(courseCode=co)
            rou.teachers.add(oo)
           
            if(teacherCount.objects.filter(firstName = oo.firstName).exists()):
                 count = teacherCount.objects.get(firstName = oo.firstName)
                 count.count = count.count+1
            else:  
                count = teacherCount() 
                count.firstName = oo.firstName
                count.lastName = oo.lastName
                count.count = count.count+1
            count.save()
        rou=routine.objects.filter(courseCode=co)
        response='/'
        return render(request,'authentication/showRoutine4.html')
    
    return render(request,'authentication/createRoutine44.html',cont)


def showRoutine4(request):
    routines = routine.objects.filter(semester="4")
    for routin in routines:
        for teacher in routin.teachers.all():
            print(teacher)
    return render(request,'authentication/showRoutine4.html',{'routines':routines})

def invisilatorsList(request):
    invisilators = teacherCount.objects.all()
    return render(request,"authentication/invisilatorList.html",{'invisilators':invisilators})