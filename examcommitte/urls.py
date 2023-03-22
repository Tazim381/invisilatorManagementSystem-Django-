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
   
   
]
