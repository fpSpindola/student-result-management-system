from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.create_student, name='add_student'),
    path('student_list/', views.list_students, name='student_list'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
]
