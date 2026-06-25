from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from . import views
from . import api_views

router = DefaultRouter()
router.register(r'departments', api_views.DepartmentViewSet)
router.register(r'subjects', api_views.SubjectViewSet)
router.register(r'teachers', api_views.TeacherViewSet)
router.register(r'students', api_views.StudentViewSet)

urlpatterns = [
   path('api/', include(router.urls)),
   path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
   path('',views.index ,name='index'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('dashboard/teacher/', views.teacher_dashboard, name='teacher_dashboard'),
   path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
   path('teachers/', views.teacher_list, name='teacher_list'),
   path('teachers/add/', views.teacher_form, name='teacher_add'),
   path('teachers/edit/', views.teacher_form, name='teacher_edit'),
   path('teachers/view/', views.teacher_detail, name='teacher_detail'),
   path('students/', views.student_list, name='student_list'),
   path('students/add/', views.student_form, name='student_add'),
   path('students/edit/', views.student_form, name='student_edit'),
   path('students/view/', views.student_detail, name='student_detail'),
   path('departments/', views.department_list, name='department_list'),
   path('departments/add/', views.department_form, name='department_add'),
   path('departments/edit/', views.department_form, name='department_edit'),
   path('subjects/', views.subject_list, name='subject_list'),
   path('subjects/add/', views.subject_form, name='subject_add'),
   path('subjects/edit/', views.subject_form, name='subject_edit'),
]
