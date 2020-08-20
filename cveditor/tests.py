from django.test import TestCase
from django.urls import resolve
from blog.views import home
from cveditor.views import cv_edit
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)
        
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        html = response.content.decode('utf8')
        #self.assertTrue(html.startswith('<html>'))
        self.assertIn('<h1 class="center">Hi!</h1>', html)
        self.assertTrue(html.endswith('</html>'))
        
        
class CVPageTest(TestCase):
    
    def test_cv_url_resolves_to_cv_editor_page(self):
        found = resolve('/cvedit')
        self.assertEqual(found.func, cv_edit)
        
    def test_cv_edit_page_returns_correct_html(self):
        request = HttpRequest()
        response = cv_edit(request)
        html = response.content.decode('utf8')
        expected_html = render_to_string('cveditor/cv_edit.html')
        self.assertEqual(html, expected_html)