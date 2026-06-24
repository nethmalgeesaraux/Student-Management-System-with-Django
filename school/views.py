from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')

def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def teacher_list(request):
    return render(request, 'teacher_list.html')

def teacher_form(request):
    return render(request, 'teacher_form.html')

def teacher_detail(request):
    return render(request, 'teacher_detail.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_form(request):
    return render(request, 'student_form.html')

def student_detail(request):
    return render(request, 'student_detail.html')

def department_list(request):
    return render(request, 'department_list.html')

def department_form(request):
    return render(request, 'department_form.html')

def subject_list(request):
    return render(request, 'subject_list.html')

def subject_form(request):
    return render(request, 'subject_form.html')
    
