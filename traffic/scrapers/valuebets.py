import sys, os, django
from selenium.webdriver import ChromeOptions, Chrome
from webdriver_manager.chrome import ChromeDriverManager
import bs4
from time import sleep
import re
from django.core.wsgi import get_wsgi_application

sys.path.append('C:\\Users\\Asen\\Desktop\\bethub\\bethub')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bethub.settings')
django.setup()
application = get_wsgi_application()

from traffic.models import ValueBets


class ValueBet:
    WEB_LINKS = {
        "football": "https://m.forebet.com/en/value-bets"
    }

    REGEX = {
        "home": r'[e][T][e][a][m]\"\>\<[s][p][a][n]\>(.{1,60})\<\/[s][p][a][n]\>\<\/[s][p][a][n]\>\<[s]',
        "away": r'[y][T][e][a][m]\"\>\<[s][p][a][n]\>(.{1,60})\<\/[s][p][a][n]\>\<\/[s][p][a][n]\>\<[s]',
        "date_and_time": r'\"\>(\d{1,2}\/\d{1,2}\/\d{4})[ ](\d{1,2}\:\d{1,2})\<\/',
        "probabilities": r'\>(\d{1,2})\<\/([t]|[b])',
        "prediction": r'[t]\"\>([A-z0-9])\<\/',
        "odd_for_prediction": r'\;\"\>(\d{1,3}\.\d{1,2})\<\/',
        "value_percent": r'[b]\>(\d{1,3})\%',
        "all_odds": r'[n]\>(\d{1,3}\.\d{1,2})\<\/',
    }

    def scrape(self):

        # OPEN THE BROWSER
        driver = self.open_the_browser()

        # GET THE HTML DATA
        all_games = self.get_the_data(driver)

        # GET THE GAMES FROM THE DATA
        self.clean_data(all_games)

    def open_the_browser(self):
        options = ChromeOptions()
        options.headless = True  # -> FALSE IF YOU WANT TO SEE THE BROWSER BROWSING
        driver = Chrome(options=options, executable_path=ChromeDriverManager().install())
        driver.get(self.WEB_LINKS["football"])
        sleep(3)
        driver.find_element_by_css_selector('#close-cc-bar').click()
        return driver

    def clean_data(self, all_games):
        the_bulk = []
        for game in all_games:
            # STORE ALL THE ITEMS
            [date, time, home, away, home_prob, draw_prob, away_prob, prediction,
             odds_for_pred, value_percent, home_odd, draw_odd, away_odd] = ['', '', '', '', '', '',
                                                                            '', '', '', '', '', '', '']

            # FIND THE TEAMS
            try:
                home = re.search(self.REGEX["home"], str(game)).group(1)
                away = re.search(self.REGEX["away"], str(game)).group(1)
            except AttributeError:
                continue

            # FIND DATE AND TIME
            try:
                date_and_time = re.search(self.REGEX["date_and_time"], str(game))
                date_t = date_and_time.group(1).split('/')[::-1]
                date = f"{'-'.join(date_t)}"
                time = date_and_time.group(2)
            except AttributeError:
                pass

            # FIND THE PROBABILITIES
            probabilities = re.findall(self.REGEX["probabilities"], str(game))
            home_prob = probabilities[0][0]
            draw_prob = probabilities[1][0]
            away_prob = probabilities[2][0]

            # FIND THE PREDICTION
            prediction = re.search(self.REGEX["prediction"], str(game)).group(1)

            # FIND THE ODD
            odds_for_pred = re.search(self.REGEX["odd_for_prediction"], str(game)).group(1)

            # FIND THE VALUE PERCENT
            value_percent = re.search(self.REGEX["value_percent"], str(game)).group(1)

            # FIND THE ODDS
            try:
                odds = re.findall(self.REGEX["all_odds"], str(game))
                home_odd = odds[0]
                draw_odd = odds[1]
                away_odd = odds[2]
            except AttributeError:
                home_odd, draw_odd, away_odd = ['1.00', '1.00', '1.00']

            the_bulk.append(ValueBets(date=date, time=time, home_team=home, away_team=away, home_prob=home_prob,
                                      draw_prob=draw_prob, away_prob=away_prob, bet_sign=prediction,
                                      odds_for_pred=odds_for_pred, home_odd=home_odd, draw_odd=draw_odd,
                                      away_odd=away_odd, value_percent=value_percent))

        ValueBets.objects.all().delete()
        ValueBets.objects.bulk_create(the_bulk)

    @staticmethod
    def get_the_data(driver):
        # GET THE HTML
        html = driver.execute_script('return document.documentElement.outerHTML;')

        # CLOSE THE BROWSER
        driver.close()

        # WORK WITH THE DATA
        soup = bs4.BeautifulSoup(html, 'html.parser')
        matches_one = soup.find_all(class_='tr_1')
        matches_two = soup.find_all(class_=re.compile('tr_0'))
        all_games = []
        all_games += [list(game) for game in matches_one]
        all_games += [list(game) for game in matches_two]
        return all_games
