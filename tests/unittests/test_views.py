from django.test import TestCase, Client
from django.urls import reverse


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_student_view(self):
        response = self.client.get(reverse('add_student'))
        self.assertEqual(response.status_code, 200)

    def test_student_list_view(self):
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)

    def test_add_course_view(self):
        response = self.client.get(reverse('create_course'))
        self.assertEqual(response.status_code, 200)

    def test_course_list_view(self):
        response = self.client.get(reverse('course_list'))
        self.assertEqual(response.status_code, 200)

    def test_add_result_view(self):
        response = self.client.get(reverse('add_result'))
        self.assertEqual(response.status_code, 200)

    def test_result_list_view(self):
        response = self.client.get(reverse('result_list'))
        self.assertEqual(response.status_code, 200)