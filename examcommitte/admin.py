from django.contrib import admin
from .models import teacher,student,course,createdExamCommittee

admin.site.register(teacher)
admin.site.register(student)
admin.site.register(course)
admin.site.register(createdExamCommittee)