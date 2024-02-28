from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name}   {self.family_name}"