from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher, Student

class Info:
    teachers = Teacher.objects.all()
    students = Student.objects.all()

def index(request):
    return render(request, 'journal/index.html', {
        'teachers': Teacher.objects.all(),
        'students': Student.objects.all(),
        'title': 'Journal',
    })
