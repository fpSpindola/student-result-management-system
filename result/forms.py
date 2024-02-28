from django import forms
from .models import Result
from course.models import Course
from students.models import Student


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['course', 'student', 'score']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.all()
        self.fields['student'].queryset = Student.objects.all()
        self.fields['score'].widget = forms.Select(choices=Result.score_choices)