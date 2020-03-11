import json

from django.test import TestCase
from ..models import Product


class TestViews(TestCase):
    """ class that test the view of the 'offapi' app """
    
    def setUp(self):
        """ Setup the product needed for the test to perform """
        nutriments = {"saturated-fat_100g": 2}
        test_product = Product.objects.create(product_id=124578, product_name='produit 1',nutriscore="a", nutriments=json.dumps(nutriments))
        test_product.save()

    def test_product_view(self):
        """ test that the product page is correctly loading """
        resp = self.client.get('/product/124578/')

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'offapi/product.html')

    def test_product_dont_exist(self):
        """ test that the product page is correctly loading """
        resp = self.client.get('/product/1578/')

        self.assertEqual(resp.status_code, 302)