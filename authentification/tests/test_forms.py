from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from authentification.models import User

from ..forms import UserRegisterForm, UserUpdateForm


class TestForms(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(
            username='rien42@g.com', password='1X<ISRUkw+tuK')
        test_user1.save()

    def test_userregisterform_success(self):
        """ test that the 'userregisterform' is working """
        form_data = {'username': 'rien@g.com',
                     'password1': '1X<ISRUkw+tuK', 'password2': '1X<ISRUkw+tuK'}
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_userregisterform_failed(self):
        """ test that the 'userregisterform' is failling when two different password
            have been provided or a wrong format email have been given """
        form_data = {'username': 'rien@g.com',
                     'password1': '1X<ISRUkw+tuK', 'password2': '1X<+tuK'}
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

        form_data = {'username': 'rien',
                     'password1': '1X<ISRUkw+tuK', 'password2': '1X<ISRUkw+tuK'}
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_userupdateform_success(self):
        """ test that the user profil update form is working """
        user_logged = User.objects.get(username='rien42@g.com')
        testfile = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b')
        form_data = {'first_name': 'nathan', 'last_name': 'mimoun'}
        form_file = {'image': SimpleUploadedFile(
            'myimage.jpg', testfile, content_type='image/jpeg')}
        form = UserUpdateForm(
            data=form_data, files=form_file, instance=user_logged)

        self.assertTrue(form.is_valid())
        self.assertEqual(user_logged.first_name, 'nathan')
        self.assertEqual(user_logged.last_name, 'mimoun')
        self.assertEqual(user_logged.image, 'myimage.jpg')
