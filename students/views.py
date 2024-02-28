from django.shortcuts import render, redirect, get_object_or_404

from course.models import Course
from students.forms import StudentForm
from students.models import Student


# Create your views here.
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
            # Redirect to a success page or do something else
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})


def list_students(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return redirect('student_list')
