from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="singup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="singout"),
    path('assignStudents', views.assignStudents, name="assignStudents"),
    path('teachersList', views.teachersList, name="teachersList"),
    path('createexamcommittee',views.createExamCommittee, name="createexamcommittee"),
    path('showexamcommitteehome',views.showExamCommitteeHome, name="showexamcommitteehome"),
    path('showexamcommittee1',views.showExamCommittee1, name="showexamcommittee1"),
    path('showexamcommittee2',views.showExamCommittee2, name="showexamcommittee2"),
    path('showexamcommittee3',views.showExamCommittee3, name="showexamcommittee3"),
    path('showexamcommittee4',views.showExamCommittee4, name="showexamcommittee4"),
    path('showexamcommittee5',views.showExamCommittee5, name="showexamcommittee5"), 
    path('createCourse',views.createCourse, name="createCourse"), 
    path('createdExamCommittee',views.createdexamcommittee, name="createdExamComiittee"),  
    path('createRoutine1',views.createRoutine1, name="createRoutine1"),  
    path('createRoutine11/<int:id>/<int:id2>/',views.createRoutine11,name='createRoutine11'),
    path('showRoutine1',views.showRoutine1, name="showRoutine1"), 
     path('createRoutine2',views.createRoutine2, name="createRoutine2"),  
    path('createRoutine22/<int:id>/<int:id2>/',views.createRoutine22,name='createRoutine22'),
    path('showRoutine2',views.showRoutine2, name="showRoutine2"), 
]
