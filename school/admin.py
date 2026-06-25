from django.contrib import admin
from .models import Department, Subject, Teacher, Student

admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
