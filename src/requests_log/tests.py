from django.test import TestCase

from models import RequestsLogItem


class SimpleTest(TestCase):
    def test_requests_page_exists(self):
        """
        Tests that requests page exists.
        """
        response = self.client.get('/requests/')
        self.assertEqual(response.status_code, 200)

    def test_request_is_saved(self):
        """
        Test that requests is saved into database.
        """
        self.client.get('/')
        self.assertTrue(len(RequestsLogItem.objects.all()) > 0)

    def test_requests_appear(self):
        response = self.client.get('/requests/')
        # each request is in <li> in template
        self.assertTrue('<li>' in response.content)
