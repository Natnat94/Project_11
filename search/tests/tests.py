from django.test import TestCase, Client
from offapi.models import Product, Category


class TestViews(TestCase):
    """ class that test the view of the 'search' app """

    def setUp(self):
        # setup for the two fist test
        Category.objects.create(name="category 1")
        Category.objects.create(name="category 2")
        a = Product.objects.create(
            product_id='5449000000996', product_name='produit 1', nutriscore="d")
        a.category_id.add(Category.objects.get(name="category 1"))
        a = Product.objects.create(
            product_id='3068320114453', product_name='produit 2', nutriscore="a")
        a.category_id.add(Category.objects.get(name="category 1"))
        a = Product.objects.create(
            product_id='3068456444111', product_name='produit 3', nutriscore="a")
        a.category_id.add(Category.objects.get(name="category 2"))
        a = Product.objects.create(
            product_id='3068456444123', product_name='produit 3', nutriscore="e")
        a.category_id.add(Category.objects.get(name="category 1"))

        # setup for the pagination test
        Category.objects.create(name="category 3")
        number_of_products = 13
        product_id = 5449000045712
        for product_number in range(number_of_products):
            product_id = product_id + product_number
            a = Product.objects.create(product_id=str(product_id),
                                       product_name='pagination ' +
                                       str(product_number),
                                       nutriscore="a")
            a.category_id.add(Category.objects.get(name="category 3"))

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

    def test_pagination_is_working(self):
        """ test that the pagination is working """
        resp = self.client.get('/search/', {'q': 'pagination'})

        self.assertEquals(resp.context['products'].paginator.num_pages, 2)

    def test_pagination_is_nine(self):
        """ test that the pagination is creating a new page after nine products displayed """
        resp = self.client.get('/search/', {'q': 'pagination'})

        self.assertEquals(len(resp.context['products'].object_list), 9)

