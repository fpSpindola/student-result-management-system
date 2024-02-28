from django.test import TestCase, Client
from django.urls import reverse
from course.models import Course
from students.models import Student
from result.models import Result


class ViewsIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_student_form_submission(self):
        response = self.client.post(reverse('add_student'), {
            'first_name': 'John',
            'family_name': 'Doe',
            'date_of_birth': '1990-01-01',
            'email': 'johndoe@example.com'
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful form submission

    def test_add_course_form_submission(self):
        response = self.client.post(reverse('create_course'), {
            'course_name': 'Mathematics'
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful form submission

    def test_add_result_form_submission(self):
        # Create a Student and Course first
        student = Student.objects.create(first_name='Alice', family_name='Smith', date_of_birth='1995-02-15', email='alice@example.com')
        course = Course.objects.create(course_name='Physics')

        response = self.client.post(reverse('add_result'), {
            'course': course.id,
            'student': student.id,
            'score': 'A'
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful form submission

    def test_student_list_contains_student(self):
        student = Student.objects.create(first_name='Bob', family_name='Johnson', date_of_birth='1998-03-20', email='bob@example.com')
        response = self.client.get(reverse('student_list'))
        self.assertContains(response, student.first_name)

    def test_course_list_contains_course(self):
        course = Course.objects.create(course_name='Chemistry')
        response = self.client.get(reverse('course_list'))
        self.assertContains(response, course.course_name)

    def test_result_list_contains_result(self):
        student = Student.objects.create(first_name='Eve', family_name='Brown', date_of_birth='1997-07-10', email='eve@example.com')
        course = Course.objects.create(course_name='Biology')
        result = Result.objects.create(course=course, student=student, score='B')
        response = self.client.get(reverse('result_list'))
        self.assertContains(response, student.first_name)
        self.assertContains(response, course.course_name)
        self.assertContains(response, result.score)
