from django.db import models

# Create your models here.
from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name
