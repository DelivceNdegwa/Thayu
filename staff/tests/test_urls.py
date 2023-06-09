from django.test import SimpleTestCase
from django.urls import reverse, resolve
from staff.views import *


class TestUrls(SimpleTestCase):
    def test_dashboard_url_resolve(self):
        url = reverse("staff:dashboard")
        
        self.assertEqual(resolve(url).func, dashboard)