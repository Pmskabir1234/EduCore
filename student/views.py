from django.shortcuts import render
from .models import courses,students

# Create your views here.
def home(request):
    return render(request, 'student/home.html',{})

def course(request):
    course = courses.objects.all()

    return render(request, 'student/course.html',{"courses":course})

def student_details(request):
    det = students.objects.all()

    return render(request, 'student/details.html',{'students':det})