# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1665042/data/www/creplace.ru/mysite/')
sys.path.insert(1, '/var/www/u1665042/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()