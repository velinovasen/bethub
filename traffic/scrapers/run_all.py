import sys, os, django
from django.core.wsgi import get_wsgi_application


sys.path.append('C:\\Users\\Asen\\Desktop\\bethub\\bethub')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bethub.settings')
django.setup()
application = get_wsgi_application()

from traffic.scrapers import volume_scraper
from traffic.scrapers.predictor import Predictions
from traffic.scrapers.valuebets import ValueBets


if __name__ == '__main__':
    volume_scraper.scrape()

    predictions = Predictions()
    predictions.scrape()

    vb = ValueBets()
    vb.scrape()
