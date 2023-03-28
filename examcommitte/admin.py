from django.contrib import admin
from .models import teacher,student,course,createdExamCommittee,Semister,routine,teacherCount

admin.site.register(teacher)
admin.site.register(student)
admin.site.register(course)
admin.site.register(createdExamCommittee)
admin.site.register(Semister)
admin.site.register(routine)
admin.site.register(teacherCount)