from django.test import TestCase
from django.contrib.auth.models import User
from .models import Todo

class TodoTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(username='testuser1', password='abc123')
        testuser1.save()

        # Create a todo
        test_todo = Todo.objects.create(author=testuser1, title='todo title', body='body content...')
        test_todo.save()

    def test_todo_content(self):
        todo = Todo.objects.get(id=1)
        author = f'{todo.author}'
        title = f'{todo.title}'
        body=f'{todo.body}'
        
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'todo title')
        self.assertEqual(body, 'body content...')