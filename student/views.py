from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, "home.html")

def result(request):
    name = request.POST['name']
    age = request.POST['age']
    department = request.POST['department']

    student = Student(
        name=name,
        age=age,
        department=department
    )

    student.save()

    return render(request, "result.html", {
        'name': name,
        'age': age,
        'department': department
    })