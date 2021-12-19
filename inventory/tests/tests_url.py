from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from inventory.views import Product_List, product_detail

class SmokeTest(SimpleTestCase):

    def test_url_inventory(self):
        url = reverse("product:product_list")
        self.assertEquals(resolve(url).func.view_class, Product_List)

    def test_url_inventory_id(self):
        url = reverse("product:product_detail", args=['id'])
        self.assertEquals(resolve(url).func, product_detail)