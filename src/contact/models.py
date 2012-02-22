from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=30)
    other_contacts = models.TextField()
    photo = models.ImageField(upload_to="photo", blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
