from django.test import Client, TestCase
from django.urls import reverse
from customer.views import *

class TestViews(TestCase):
    def setup(self):
        self.client = Client()
        
    
    def test_view_index_GET(self):
        response = self.client.get(reverse('customer:index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer/index.html')
        
    
    def test_view_house_GET(self):
        response = self.client.get(reverse('customer:houses'))
        
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)
        self.assertNotEqual(response.status_code, 400)
        self.assertTemplateUsed(response, 'customer/house.html')

