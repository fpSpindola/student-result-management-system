from django.db import models

# Create your models here.

from django.db import models
from course.models import Course
from students.models import Student


class Result(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score_choices = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    ]
    score = models.CharField(max_length=1, choices=score_choices)

    def __str__(self):
        return f"{self.student} - {self.course} - {self.score}"