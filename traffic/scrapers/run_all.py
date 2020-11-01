import sys, os, django
from datetime import datetime

from django.core.wsgi import get_wsgi_application


sys.path.append('C:\\Users\\Asen\\Desktop\\bethub\\bethub')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bethub.settings')
django.setup()
application = get_wsgi_application()

from traffic.scrapers import volume_scraper
from traffic.scrapers.predictor import Predictions
from traffic.scrapers.valuebets import ValueBets
from traffic.scrapers.tomorrow_games import TomorrowGames


if __name__ == '__main__':
    file = open('run_log.txt', 'a')
    file.write(f'\nStarted at: {datetime.now()}\n')
    try:
        gms = TomorrowGames()
        gms.scrape()
        file.write('--- Games for tomorrow - DONE\n')
    except Exception:
        file.write('--- Games for tomorrow - FAILED\n')

    try:
        volume_scraper.scrape()
        file.write('--- Volume - DONE\n')
    except Exception:
        file.write('--- Volume - FAILED\n')

    try:
        predictions = Predictions()
        predictions.scrape()
        file.write('--- Predictions - DONE\n')
    except Exception:
        file.write('--- Predictions - FAILED\n')

    try:
        vb = ValueBets()
        vb.scrape()
        file.write('--- Value Bets - DONE\n')
    except Exception:
        file.write('--- Value Bets - FAILED\n')

    file.close()
