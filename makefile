test:
	python src/manage.py test contact requests_log
test_windmill:
	python src/manage.py collectstatic --noinput
	python src/manage.py test_windmill
