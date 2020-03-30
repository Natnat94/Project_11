from django.test import TestCase, Client
from django.contrib.auth.forms import PasswordChangeForm
from django.core.files.uploadedfile import SimpleUploadedFile
from authentification.models import User


class TestViews(TestCase):
    """ class that test the view of the 'authentification' app """

    def setUp(self):
        test_user1 = User.objects.create_user(
            username='rien@g.com', password='1X<ISRUkw+tuK')
        test_user1.save()

    def test_profil_view_logged(self):
        """ test that the profil view is showed when logged to the system """
        self.client.login(username='rien@g.com', password='1X<ISRUkw+tuK')
        resp = self.client.get('/profil/')

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'authentification/profil.html')

    def test_profil_view_not_logged(self):
        """ test that the profil view is showed only when logged to the system """
        resp = self.client.get('/profil/')

        self.assertEqual(resp.status_code, 302)

    def test_register(self):
        """ test the register a user view """
        c = Client()
        response = c.post('/register/', {'username': 'rie47n@g.com',
                                         'password1': '1X<ISRUkw+tuK', 
                                         'password2': '1X<ISRUkw+tuK'}, follow=True)
        user_login = self.client.login(
            username='rie47n@g.com', password='1X<ISRUkw+tuK')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(user_login)

    def test_profil(self):
        """ test the update the profil view """
        c = Client()
        c.login(username='rien@g.com', password='1X<ISRUkw+tuK')
        testfile = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b')
        image = SimpleUploadedFile(
            'nathan.jpg', testfile, content_type='image/jpeg')
        response = c.post(
            '/profil/', {'first_name': 'tata', 'last_name': 'mimi', 'image': image}, follow=True)
        user = User.objects.get(username='rien@g.com')

        self.assertEqual(response.status_code, 200)
        self.assertEqual('tata', user.first_name)
        self.assertEqual('mimi', user.last_name)
        self.assertEqual('profile_pics/nathan.jpg', user.image.name)

    def test_change_password(self):
        """ test the change the user password view """
        c = Client()
        c.login(username='rien@g.com', password='1X<ISRUkw+tuK')
        user = User.objects.get(username='rien@g.com')
        pwd = user.password

        data = {'old_password': '1X<ISRUkw+tuK',
                'new_password1': '1X<ISGHJSGJHkw+tuK', 
                'new_password2': '1X<ISGHJSGJHkw+tuK'}
        response = c.post('/profil/password/', data, follow=True)
        user = User.objects.get(username='rien@g.com')
        pwd2 = user.password

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentification/password.html')
        self.assertNotEqual(pwd, pwd2)

    def tearDown(self):
        """ remove the profile picture uploaded during the test """
        user = User.objects.get(username='rien@g.com')
        user.image.delete()
