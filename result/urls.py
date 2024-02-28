from django.urls import path
from . import views

urlpatterns = [
    path('add_result/', views.add_result, name='add_result'),
    path('result_list/', views.result_list, name='result_list'),
]
