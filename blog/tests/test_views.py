from django.test import TestCase
from authentification.models import User


class TestViews(TestCase):
    """ class that test the view of the 'blog' app """

    def setUp(self):
        """ Setup the component needed for the test to perform """
        test_user1 = User.objects.create_user(username='rien@g.com', password='1X<ISRUkw+tuK')
        test_user1.save()

    def test_home_view(self):
        """ test that the home page is correctly loading """
        resp = self.client.get('/')

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/index.html')

    def test_legal_view(self):
        """ test that the legal page is correctly loading """
        resp = self.client.get('/legal/')

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/legal.html')
