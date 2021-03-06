from django.urls import resolve
from django.template.loader import render_to_string
from django.http import HttpRequest
from django.test import TestCase

# Create your tests here.
class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
