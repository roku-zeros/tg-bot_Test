# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1813889/data/www/wolf-mag.ru/tg-bot_Test')
sys.path.insert(1, '/var/www/u1813889/data/djangoenv/lib/python3.8.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'TgSeller.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()