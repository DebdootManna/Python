from django.test import TestCase
from django.urls import reverse

class HomePageViewTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'my_app/index.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Hello, world!')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('home'))
        self.assertNotContains(response, 'Goodbye, world!')