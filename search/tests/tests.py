from django.test import TestCase
from django.test import Client
from offapi.models import Product, Category

class TestViews(TestCase):
    """ class that test the view of the 'search' app """

    def setUp(self):
        Category.objects.create(name="category 1")
        Category.objects.create(name="category 2")
        a=Product.objects.create(product_id='5449000000996', product_name='produit 1', nutriscore="d")
        a.category_id.add(Category.objects.get(name="category 1"))
        a=Product.objects.create(product_id='3068320114453', product_name='produit 2', nutriscore="a")
        a.category_id.add(Category.objects.get(name="category 1"))
        a=Product.objects.create(product_id='3068456444111', product_name='produit 3', nutriscore="a")
        a.category_id.add(Category.objects.get(name="category 2"))
        a=Product.objects.create(product_id='3068456444123', product_name='produit 3', nutriscore="e")
        a.category_id.add(Category.objects.get(name="category 1"))

    def test_search_view(self):
        """ test that a search view work correctly """
        resp = self.client.get('/search/', {'q': 'produit 1'})
        
        self.assertEqual(resp.context['products'][0].product_id, 5449000000996)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'search/search.html')

    def test_substitute_view(self):
        """ test that a substitute view work correctly """
        resp = self.client.get('/search/5449000000996/')

        for result in resp.context['products']:
            self.assertEqual(result.product_id, 3068320114453)
            self.assertNotEqual(result.product_id, 3068456444111)
            self.assertNotEqual(result.product_id, 3068456444123)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'search/search.html')
