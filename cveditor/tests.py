from django.test import TestCase
from django.urls import resolve
from blog.views import home
from cveditor.views import cv_edit
from django.http import HttpRequest
from django.template.loader import render_to_string
from cveditor.models import Item

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
        response = self.client.get('/cvedit')
        self.assertTemplateUsed(response, 'cveditor/cv_edit.html')
        
    def test_can_save_a_POST_request(self):
        self.client.post('/cvedit', data={'item_text': 'A new text item'})
        
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new text item')
        
    def test_redirects_after_POST(self):
        response = self.client.post('/cvedit', data={'item_text': 'A new text item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cvedit/the_only_CV_in_the_world/')
        
    def test_only_saves_items_when_necessary(self):
        self.client.get('/cvedit')
        self.assertEqual(Item.objects.count(), 0)

        
class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()
        
        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()
        
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
    
class CVViewTest(TestCase):

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text ='itemey 2')
        
        response = self.client.get('/cvedit/the_only_CV_in_the_world/')
        
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        
    def test_uses_list_template(self):
        response = self.client.get('/cvedit/the_only_CV_in_the_world/')
        self.assertTemplateUsed(response, 'cveditor/cv_view.html')