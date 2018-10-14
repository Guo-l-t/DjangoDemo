import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoDemo.settings'
from django.db import connection
cursor = connection.cursor()
