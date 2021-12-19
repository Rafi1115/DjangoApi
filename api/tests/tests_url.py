from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from api.views import ProductListApiView

class SmokeTest(SimpleTestCase):

    def test_url_inventory(self):
        url = reverse("api_product_list")
        self.assertEquals(resolve(url).func.view_class, ProductListApiView)
