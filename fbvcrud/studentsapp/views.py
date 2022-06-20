from django.shortcuts import render, redirect
from .models import Student
from .forms import Studentform


# Create your views here.

def home(request):
    template_name = "home.html"
    context = {'home':home}
    return render(request, template_name, context)


def studentform(request):
    form = Studentform()
    if request.method == 'POST':
        form = Studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    template_name = "studentsform.html"
    context = {"form": form}
    return render(request, template_name, context)


def studentdata(request):
    student = Student.objects.all()
    template_name = "studentaspp/students.html"
    context = {"student": student}
    return render(request, template_name, context)


def delete(request, id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect('stu')


def update(request, oid):
    obj = Student.objects.get(id=oid)
    form = Studentform(instance=obj)
    if request.method == "POST":
        form = Studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stu')
    template_name = "studentsapp/studentsform.html"
    context = {'form': form}
    return render(request, template_name, context)
