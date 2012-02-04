"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.conf import settings


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
        field_names_in_view = [
                "Contacts",
                "Email",
                "Jabber",
                "Skype",
                "Other contacts",
                ]
        data_in_view = [
                "Artem",
                "Dudarev",
                "1978",
                "Donetsk",
                "gmail.com",
                "artem_dudarev",
                "twitter"
                ]
        for f in field_names_in_view:
            self.assertTrue(f in response.content)
        for d in data_in_view:
            self.assertTrue(d in response.content)

    def test_link_to_requests_page(self):
        """
        Tests that the link to requests page is present.
        """
        response = self.client.get('/')
        self.assertTrue('requests' in response.content)

    def test_author(self):
        """
        Tests that name meta tag exists. Name is obtained from settings.ADMIN.
        """
        response = self.client.get('/')
        author = '<meta name="author" content="%s" />' % settings.ADMINS[0][0]
        self.assertTrue(author in response.content)

    def test_edit_page_exists(self):
        """
        Test that page /edit exists.
        """
        response = self.client.get('/edit')
        self.assertEqual(response.status_code, 200)
