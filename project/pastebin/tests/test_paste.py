from rest_framework.test import APITestCase
from django.test import Client
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from django.db.models import Count

from project.pastebin.models import Paste
from project.pastebin.serializers import PasteSerializer, UserStatisticSerializer


# initialize the APIClient app
client = Client()

class TestPasteModel(APITestCase):
    """basic test cases for paste model"""
    def setUp(self):
        self.paste = Paste.objects.create(
            text='text', user=get_user_model().objects.create(
                username='testuser', password='test1234'
            )
        )

    def test_get_all_pastes(self):
        # get API response
        response = client.get(reverse('all-pastes'))
        # get data from db
        pastes = Paste.objects.all()
        serializer = PasteSerializer(pastes, many=True)
        self.assertEqual(response.data.get('results'), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_paste(self):
        response = client.get(
            reverse('paste-detail', kwargs={'slug': self.paste.slug}))
        paste = Paste.objects.get(slug=self.paste.slug)
        serializer = PasteSerializer(paste)
        self.assertEqual(response.data.get('data'), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_statistics(self):
        # get API response
        response = client.get(reverse('statistics'))
        # get data from db
        statistics = get_user_model().objects.annotate(pastes_count=Count('pastes')).order_by('-pastes_count')[:5]
        serializer = UserStatisticSerializer(statistics, many=True)
        self.assertEqual(response.data.get('results'), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)