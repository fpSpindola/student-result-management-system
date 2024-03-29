from django import forms
from .models import Student
from .validators import validate_age


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'family_name', 'date_of_birth', 'email']

    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        validate_age(dob)
        return dob

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})