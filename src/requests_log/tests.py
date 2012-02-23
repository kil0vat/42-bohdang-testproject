from django.test import TestCase
from django.core.urlresolvers import reverse

from models import RequestsLogItem


class RequestsLogTest(TestCase):
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
        # each request is in <td> in template
        self.assertTrue('<td' in response.content)

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

    def test_request_has_default_priority(self):
        r = RequestsLogItem(
                path='/',
                method='GET',
                META=''
                )
        r.save()
        self.assertEqual(r.priority, 1)

    def test_update_priority(self):
        # check that pk=1 exists, if not - create
        try:
            r = RequestsLogItem.objects.get(pk=1)
        except:
            r = RequestsLogItem(
                    pk=1,
                    path='/',
                    method='GET',
                    META=''
                    )
            r.save()
        def assertPriorityUpdate(self, new_priority):
            self.client.post(reverse('update_priority'), 
                    {
                        'id':1,
                        'priority': new_priority
                    })
            r = RequestsLogItem.objects.get(pk=1)
            self.assertEqual(r.priority,new_priority)
        new_priority = 0
        assertPriorityUpdate(self, new_priority)
        new_priority = 1
        assertPriorityUpdate(self, new_priority)
