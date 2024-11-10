from django.contrib import admin
from .models import Subject, Student, Teacher, Grade, Schedule

admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Grade)
admin.site.register(Schedule)