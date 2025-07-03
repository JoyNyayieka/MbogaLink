from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from myapp.views import stk
from django.http import JsonResponse


# Create your tests here.
class SimpleTest(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get(reverse('index'))  # actual URL name
        self.assertEqual(response.status_code, 200)


class DarajaAPITest(TestCase):

    @patch('myapp.views.requests.post')
    def test_stk_push_request(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "ResponseCode": "0",
            "CustomerMessage": "Success. Request accepted for processing"
        }

        response = self.client.post(reverse('stk'), {
            'phone': '254712345678',
            'amount': '10'
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Payment made successfully", response.content)

