SHELL=/bin/sh
MANAGE=PYTHONPATH=$(CURDIR) python manage.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=src.settings $(MANAGE) test contact_info

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=src.settings $(MANAGE) runserver

shell:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=src.settings $(MANAGE) shell

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=src.settings $(MANAGE) syncdb --noinput
	
migrate:	
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=src.settings $(MANAGE) migrate

collectstatic:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=src.settings $(MANAGE) collectstatic --noinput
