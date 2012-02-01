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

    def test_no_more_than_ten(self):
        number_of_requests = 11
        for i in range(number_of_requests):
            response = self.client.get('/requests/')
        # each request is in <li> in template
        self.assertTrue(response.content.count('<li>') < 11)

    def test_only_first_ten(self):
        # delete all requests from database
        RequestsLogItem.objects.all().delete()
        # make first request to path /requests/first_request/ - returns 404
        response = self.client.get('/requests/first_request/')
        # make 10 more requests
        number_of_requests = 10
        for i in range(number_of_requests):
            response = self.client.get('/requests/')
        # make sure that the /first_request/ path is present in the list
        self.assertTrue('/requests/first_request/' in response.content)
