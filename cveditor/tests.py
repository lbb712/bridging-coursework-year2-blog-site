from django.test import TestCase
from django.urls import resolve
from blog.views import home
from cveditor.views import cv_edit

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)
        
class CVPageTest(TestCase):
    
    def test_cv_url_resolves_to_cv_editor_page(self):
        found = resolve('/cvedit')
        self.assertEqual(found.func, cv_edit)