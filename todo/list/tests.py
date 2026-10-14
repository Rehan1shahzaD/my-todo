from django.test import TestCase

from .form import TODOForm
from .models import TODO


class TodoFormTests(TestCase):
    def test_form_accepts_title_and_description(self):
        form = TODOForm(data={'title': 'Write tests', 'description': 'Add regression coverage'})
        self.assertTrue(form.is_valid())


class TodoViewTests(TestCase):
    def test_home_page_renders_saved_tasks(self):
        TODO.objects.create(title='Write code', description='Fix the todo app')

        response = self.client.get('/')

        self.assertContains(response, 'Write code')
        self.assertContains(response, 'Fix the todo app')
