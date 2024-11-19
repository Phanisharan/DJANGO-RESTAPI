# your_app/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task
from datetime import date, timedelta
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class TaskAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a test user
        self.user = User.objects.create_user(username="phani", password="phani@123")

        # Generate a token for the test user
        self.token = Token.objects.create(user=self.user)

        # Add the token to the Authorization header
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.task_data = {
            "title": "Test Task",
            "description": "A sample task for testing",
            "due_date": str(date.today() + timedelta(days=1)),
            "status": "pending"
        }

    def test_create_task(self):
        response = self.client.post("/tasks/create/", self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("title", response.data)

    def test_mark_task_complete(self):
        task = Task.objects.create(**self.task_data)
        response = self.client.patch(f"/tasks/complete/{task.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "completed")
