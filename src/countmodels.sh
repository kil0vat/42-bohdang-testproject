#!/bin/bash

file_name=`date --rfc-3339=date`
python manage.py countmodels 2> $file_name.dat
