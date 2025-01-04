from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo


class TodoModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="First Todo",
            body="A body of text here",
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "First Todo")
        self.assertEqual(self.todo.body, "A body of text here")
        self.assertEqual(str(self.todo), "First Todo")

    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(response.data[0]["title"], "First Todo")
        self.assertEqual(response.data[0]["body"], "A body of text here")

    def test_api_detailview(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(response.data["title"], "First Todo")
        self.assertEqual(response.data["body"], "A body of text here")
