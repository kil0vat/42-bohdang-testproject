"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_requests_page_exists(self):
        """
        Tests that requests page exists.
        """
        response = self.client.get('/requests/')
        self.assertEqual(response.status_code, 200)
