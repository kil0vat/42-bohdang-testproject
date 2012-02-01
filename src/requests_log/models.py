from django.db import models


class RequestsLogItem(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=2048)
    method = models.CharField(max_length=4)
    META = models.TextField()
    
    def __unicode__(self):
        return u'%s' % (self.time)
