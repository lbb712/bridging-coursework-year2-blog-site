from django.test import TestCase
from django.urls import resolve
from blog.views import post_list
from django.http import HttpRequest
from blog.models import Post
from django.contrib.auth.models import User


class PostListTest(TestCase):
        
    def test_base_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/base.html')
        
class ItemModelTest(TestCase):
  
    def test_saving_and_retrieving_items(self):
        user = User(username='username')
        user.save()
        
        first_item = Post()
        first_item.author = user
        first_item.title = 'Test1'
        first_item.text = 'The first blog item'
        first_item.save()
        
        second_item = Post()
        second_item.author = user
        second_item.title = 'Test2'
        second_item.text = 'Blog item the second'
        second_item.save()
        
        saved_items = Post.objects.all()
        self.assertEqual(saved_items.count(), 2)
        
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first blog item')
        self.assertEqual(second_saved_item.text, 'Blog item the second')
        
   