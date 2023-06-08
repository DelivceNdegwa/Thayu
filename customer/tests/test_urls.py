from django.test import SimpleTestCase
from django.urls import reverse, resolve
from customer.views import *


class TestUrl(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse("customer:index")
        
        self.assertEqual(resolve(url).func, index)
        
    def test_houses_url_is_resolved(self):
        url = reverse("customer:houses")
        
        self.assertEqual(resolve(url).func, houses)
        
    def test_properties_url_is_resolved(self):
        url = reverse("customer:properties")
        
        self.assertEqual(resolve(url).func, properties)
        
    def test_contact_url_is_resolved(self):
        url = reverse("customer:contact")
        
        self.assertEqual(resolve(url).func, contact)
        
    def test_send_message_url_is_resolved(self):
        url = reverse("customer:send-message")
        
        self.assertEqual(resolve(url).func, send_message)