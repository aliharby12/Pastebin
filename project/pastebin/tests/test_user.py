from rest_framework.test import APITestCase
from django.test import Client
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.hashers import make_password

from project.pastebin.models import Country

# initialize the APIClient app
client = Client()


class TestPasteModel(APITestCase):
    """basic test cases for paste model"""
    def setUp(self):
        self.country = Country.objects.create(title='test country')
        self.username = 'testuser'
        self.password = 'test1234'

    def test_register_user(self):
        response = client.post(reverse('user-register'), data={
            'username': self.username,
            'password': self.password,
            'country' : self.country.pk
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_login_user(self):
        client.post(reverse('user-register'), data={
            'username': self.username,
            'password': self.password,
            'country' : self.country.pk
        })
        response = client.post(reverse('login-with-token'), data={
            'username':self.username, 'password':self.password
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)