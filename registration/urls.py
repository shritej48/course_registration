from django.urls import path
from . import views

urlpatterns = [
    # Auth / general
    path('', views.login_page, name='login'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout_page, name='logout'),   # ← ADD THIS LINE

    # Course
    path('course/', views.course_show, name='course_show'),
    path('course/create/', views.course_create, name='course_create'),
    path('course/update/<int:cid>/', views.course_update, name='course_update'),
    path('course/delete/<int:cid>/', views.course_delete, name='course_delete'),

    # Student
    path('student/', views.student_show, name='student_show'),
    path('student/create/', views.student_create, name='student_create'),
    path('student/update/<int:sid>/', views.student_update, name='student_update'),
    path('student/delete/<int:sid>/', views.student_delete, name='student_delete'),

    # Enrollment
    path('enrollment/', views.enrollment_show, name='enrollment_show'),
    path('enrollment/create/', views.enrollment_create, name='enrollment_create'),
    path('enrollment/update/<int:eid>/', views.enrollment_update, name='enrollment_update'),
    path('enrollment/delete/<int:eid>/', views.enrollment_delete, name='enrollment_delete'),
]