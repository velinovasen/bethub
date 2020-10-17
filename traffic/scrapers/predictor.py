import sys, os, django
from selenium.webdriver import ChromeOptions, Chrome
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from time import sleep
import re
from django.core.wsgi import get_wsgi_application

sys.path.append('C:\\Users\\Asen\\Desktop\\bethub\\bethub')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bethub.settings')
django.setup()
application = get_wsgi_application()
