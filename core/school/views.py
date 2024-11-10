from django.shortcuts import render
from . import models

def teacher_list(request):
    teachers = models.Teacher.objects.all()
    context = {
        "teachers": teachers
    }

    return render(request, 'teacher_list.html', context)