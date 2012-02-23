from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('requests_log.views',
    url(r'^$', 'index', name='requests_log'),
    url(r'^update_priority/$', 'update_priority', name='update_priority'),
)
