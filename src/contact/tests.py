"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from bs4 import BeautifulSoup as bs

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.conf import settings

from models import Contact



class ContactTestCase(TestCase):
    def test_index(self):
        """
        Tests that index page exists.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_static_style_css(self):
        """
        Tests that style css page exists. This is to make sure that static content is served by test server where DEBUG=False
        """
        response = self.client.get('/static/css/style.css')
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
    
    def test_login_exists(self):
        """
        Tests that the link to login exists.
        """
        response = self.client.get('/')
        self.assertTrue('Login' in response.content)
    
    def test_accounts_profile_redirects(self):
        """
        Tests that accounts/profile redirects to existing page.
        """
        User.objects.create_user('test', 'dudarev+test@gmail.com', 'test')
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('profile'), follow="True")
        self.assertEqual(response.status_code, 200)

    def test_edit_logout_when_logged_in(self):
        """
        Tests that 'Edit | Logout' links exist when logged in.
        """
        User.objects.create_user('test', 'dudarev+test@gmail.com', 'test')
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('index'))
        self.assertTrue('Logout' in response.content)
        self.assertTrue('Edit' in response.content)
        self.assertFalse('Login' in response.content)


class EditContactTestCaseNonAuth(TestCase):
    def test_edit_page_exists(self):
        """
        Test that page /edit/ exists and redirects if user is not logged in.
        """
        response = self.client.get('/edit/')
        self.assertEqual(response.status_code, 302)
    
    def test_edit_page_redirects(self):
        """
        Test that page /edit/ redirects to /accounts/login/?next=/edit/.
        """
        response = self.client.get('/edit/', follow=True)
        last_redirect = response.redirect_chain[-1][0]
        self.assertTrue("/accounts/login/?next=/edit/" in last_redirect)

    def test_redirect_from_edit_exists(self):
        """
        Test that page where /edit/ redirects exits.
        """
        response = self.client.get('/edit/', follow=True)
        self.assertEqual(response.status_code, 200)


class EditContactTestCaseAuth(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test', 'dudarev+test@gmail.com', 'test')
        self.client.login(username='test', password='test')
        self.response = self.client.get(reverse('edit_contact'))

    def test_user_may_login(self):
        """
        Test that a user created in setUp may login.
        """
        self.assertEqual(self.response.status_code, 200)

    def test_form_exists(self):
        """
        Test that a form exists on /edit/ page.
        """
        self.assertTrue('<form' in self.response.content)

    def test_cancel_button_exists(self):
        """
        Test that cancel button exists on /edit/ page.
        """
        self.assertTrue('Cancel' in self.response.content)

    def test_default_values(self):
        """
        Test that default values are in the form.
        """
        contact = Contact.objects.get(pk=1)
        self.assertTrue(self.response.content.decode('utf8').find(contact.skype) >= 0)

    def test_calendar_div(self):
        """
        Test that there is a calendar div for birth date (instead of just input).
        """
        soup = bs(self.response.content)
        self.assertEqual(soup.find(id="id_birth_date")['type'], 'hidden')


class EditContactTestCasePost(TestCase):
    def setUp(self):
        """
        Set up login.
        """
        self.user = User.objects.create_user('test', 'dudarev+test@gmail.com', 'test')
        self.client.login(username='test', password='test')
        self.good_data = {
                "is_ajax_request": 0,
                "bio": "Artem was born in Donetsk", 
                "first_name": "Artem",
                "last_name": "Dudarev", 
                "other_contacts": "http://twitter.com/dudarev", 
                "skype": "artem_dudarev", 
                "birth_date": "1978-08-07", 
                "jabber": "dudarev@gmail.com", 
                "email": "dudarev@gmail.com"
                }

    def test_send_no_data(self):
        """
        Test when no data is sent.
        """
        response = self.client.post(reverse('edit_contact'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form']['first_name'].errors, [u'This field is required.'])

    def test_send_good_data_updates(self):
        """
        Test that when good data is sent contact is updated.
        """
        test_name = "Another Name"
        self.good_data['first_name'] = test_name
        self.client.post(reverse('edit_contact'), self.good_data)
        contact = Contact.objects.get(pk=1)
        self.assertEqual(contact.first_name, test_name)

    def test_send_good_data_redirects(self):
        """
        Test that when good data is sent one is redirected.
        """
        response = self.client.post(reverse('edit_contact'), self.good_data, follow=True)
        self.assertEqual(response.status_code, 200)


# TODO: (for future consideration)
# include windmill tests here
# presently with
# $ python manage.py test_windmill

"""
import os
from windmill.authoring import djangotest 

class TestProjectWindmillTest(djangotest.WindmillDjangoUnitTest): 
        test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'windmilltests')
        browser = 'firefox'
"""
