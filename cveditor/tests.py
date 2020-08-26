from django.test import TestCase
from django.urls import resolve
from blog.views import home
from cveditor.views import cv_list
from django.http import HttpRequest
from django.template.loader import render_to_string
from cveditor.models import CV
from cveditor.forms import CVForm, EMPTY_FIELD_ERROR


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)
        
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        html = response.content.decode('utf8')
        self.assertIn('<h1 class="center">Hi!</h1>', html)
        self.assertTrue(html.endswith('</html>'))
        
        
class CVPageTest(TestCase):
    
    def test_cv_url_resolves_to_cv_editor_page(self):
        found = resolve('/cvedit/list')
        self.assertEqual(found.func, cv_list)
        
    def test_cv_edit_page_returns_correct_html(self):
        response = self.client.get('/cvedit/list')
        self.assertTemplateUsed(response, 'cveditor/cv_list.html')

        
class CVAndItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_cv = CV()
        first_cv.title = 'The first cv title'
        first_cv.name='Jane'
        first_cv.save()
        
        second_cv = CV()
        second_cv.title = 'The second cv title'
        second_cv.name = 'John'
        second_cv.save()
        
        saved_cv = CV.objects.first()
        self.assertEqual(saved_cv, first_cv)

        self.assertEqual(first_cv.title, 'The first cv title')
        self.assertEqual(first_cv.name, 'Jane')
        self.assertEqual(second_cv.title, 'The second cv title')
        self.assertEqual(second_cv.name, 'John')
   
        
class CVFormTest(TestCase):
    def test_form_renders_cv_text_input(self):
        form = CVForm()
        self.assertIn('placeholder="Enter your name"', form.as_p())
        
    def test_form_validation_for_blank_items(self):
        form = CVForm(data={'title': 'Test', 'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['name'],
            [EMPTY_FIELD_ERROR]
        )
        


    