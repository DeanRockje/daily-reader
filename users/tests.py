from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm



# Create your tests here.


class TestUserRegistration(TestCase):

    def test_valid_registration(self):
        form = RegisterForm({

            'username':'Dean',
            'password':'DeanRockje',
            'email':'test@test.com',
        })
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertTrue(user.username,'Dean')
        self.assertTrue(user.password, 'DeanRockje')
        self.assertTrue(user.email,'test@test.com')

    def test_invalid(self):
        form = RegisterForm({

            'username': 'Dean',
            'password': '',
            'email': 'test@test.com',
        })
        self.assertFalse(form.is_valid())


class TestUserAuthForm(TestCase):
    def test_invalid(self):
        """Invalid data test case"""
        form = LoginForm({
            'username':'bbbb',
            'password':'sadokowakdaw',
            })
        self.assertFalse(form.is_valid())

    def test_valid_auth(self):
        user = User.objects.create(username='Dean', password='DeanRockje', email='test@email.com')
        form = LoginForm({
            'username':user.username,
            'password':user.password,
        })

        self.assertFalse(form.is_valid())

