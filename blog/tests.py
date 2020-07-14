from django.test import TestCase
from django.urls import resolve
from blog.views import post_list
from django.http import HttpRequest


class PostListTest(TestCase):
        
    def test_base_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/base.html')
