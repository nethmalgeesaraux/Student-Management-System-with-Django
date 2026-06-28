from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, Teacher, Department, Subject

@login_required
def index(request):
    if hasattr(request.user, 'teacher'):
        return redirect('teacher_dashboard')
    elif hasattr(request.user, 'student'):
        return redirect('student_dashboard')
    return render(request, 'index.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

@login_required
def teacher_form(request):
    return render(request, 'teacher_form.html')

@login_required
def teacher_detail(request):
    return render(request, 'teacher_detail.html')

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

@login_required
def student_form(request):
    return render(request, 'student_form.html')

@login_required
def student_detail(request):
    return render(request, 'student_detail.html')

@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

@login_required
def department_form(request):
    return render(request, 'department_form.html')

@login_required
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})

@login_required
def subject_form(request):
    return render(request, 'subject_form.html')
