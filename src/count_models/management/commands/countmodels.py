from django.core.management.base import NoArgsCommand
from django.db import models

class Command(NoArgsCommand):
    help = 'Print all models and count number of elements for each of them.'

    def handle_noargs(self, *args, **options):
        ms = models.get_models()
        for m in ms:
            line = "%s: %d\n" % (m._meta.object_name, m.objects.count())
            self.stdout.write(line)
            self.stderr.write("error: "+line)
