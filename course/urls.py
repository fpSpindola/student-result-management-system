from django.urls import path

from course import views

urlpatterns = [
    path('add_course/', views.create_course, name='create_course'),
    path('course_list/', views.course_list, name='course_list'),
    path('delete_course/<int:pk>/', views.delete_course, name='delete_course'),
]