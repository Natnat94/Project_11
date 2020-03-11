from django.test import TestCase
from ..models import Category, Store, Product, ProductSaved
from authentification.models import User


# models test
class CategoryTest(TestCase):
    """ class that test the Category table of the model """
    def create_category(self, name="only a test"):
        return Category.objects.create(name=name)

    def test_category_creation(self):
        w = self.create_category()
        self.assertTrue(isinstance(w, Category))
        self.assertEqual(w.__str__(), w.name)


class StoreTest(TestCase):
    """ class that test the Store table of the model """
    def create_store(self, name="only a test"):
        return Store.objects.create(name=name)

    def test_store_creation(self):
        w = self.create_store()
        self.assertTrue(isinstance(w, Store))
        self.assertEqual(w.__str__(), w.name)


class ProductTest(TestCase):
    """ class that test the Product table of the model """
    def create_Product(self):
        return Product.objects.create(product_id=124578, product_name='produit 1')

    def test_product_creation(self):
        w = self.create_Product()
        self.assertTrue(isinstance(w, Product))
        self.assertEqual(w.__str__(), w.product_name)


class ProductSavedTest(TestCase):
    """ class that test the Product-Saved table of the model """

    def setUp(self):
        test_user1 = User.objects.create_user(username='rien@g.com', password='1X<ISRUkw+tuK')
        test_user1.save()

    def create_productsaved(self):
        user = User.objects.get(username='rien@g.com')
        product_a = Product.objects.create(product_id=124578, product_name='produit 1')
        product_b = Product.objects.create(product_id=235689, product_name='produit 2')
        return ProductSaved.objects.create(user_id=user, product_id=product_a, sub_id=product_b)

    def test_productsaved_creation(self):
        w = self.create_productsaved()
        self.assertTrue(isinstance(w, ProductSaved))
        self.assertEqual(w.__str__(), '{} - {}'.format(w.user_id, w.product_id))
