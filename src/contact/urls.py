from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('contact.views',
    url(r'^$', 'index', name='index'),
    url(r'^edit/$', 'edit_contact', name='edit_contact'),
)
