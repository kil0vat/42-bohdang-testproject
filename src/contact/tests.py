"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class ContactTestCase(TestCase):
    def test_index(self):
        """
        Tests that index page exists.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_content(self):
        """
        Tests that data exists in the view.
        """
        response = self.client.get('/')
        self.assertTrue("Artem Dudarev" in response.content)
