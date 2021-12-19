from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('get-number')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
