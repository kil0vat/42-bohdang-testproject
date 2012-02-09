from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import redirect_to

urlpatterns = patterns('contact.views',
    url(r'^$', 'index', name='index'),
    url(r'^accounts/profile/$', redirect_to, {'url': '/'}, name='profile'),
    url(r'^edit/$', 'edit_contact', name='edit_contact'),
)
