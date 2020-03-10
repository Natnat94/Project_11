from django.test import TestCase
from authentification.models import User
from offapi.models import Product, ProductSaved


class TestViews(TestCase):
    """ class that test the view of the 'addfav' app """

    def setUp(self):
        test_user1 = User.objects.create_user(username='rien@g.com', password='1X<ISRUkw+tuK')
        test_user1.save()
        Product.objects.create(product_id='5449000000996', product_name='produit 1')
        Product.objects.create(product_id='3068320114453', product_name='produit 2')

    def test_add_view(self):
        """ test that a product match is saved as favorite """
        self.client.login(username='rien@g.com', password='1X<ISRUkw+tuK')
        resp = self.client.post('/search/5449000000996/3068320114453/')
        # print(resp.context)
        # self.assertEqual(resp.status_code, 200)


    def test_favorite_view(self):
        """ test that the favorite view is display """
        self.client.login(username='rien@g.com', password='1X<ISRUkw+tuK')
        resp = self.client.get('/favorite/')

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'addfav/display.html')
