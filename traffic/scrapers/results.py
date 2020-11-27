import json
import sys, os, django

from django.core import serializers
from selenium.webdriver import ChromeOptions, Chrome
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from time import sleep
import re
from datetime import datetime, timedelta
from django.core.wsgi import get_wsgi_application

sys.path.append('C:\\Users\\Asen\\Desktop\\bethub\\bethub')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bethub.settings')
django.setup()
application = get_wsgi_application()

from traffic.models import RegularGame, ResultGame


def get_yesterday_date():
    datetime.today().strftime('%Y-%m-%d')
    tomorrow_date = (datetime.today() - timedelta(hours=24)).strftime('%Y-%m-%d')
    return "".join(tomorrow_date.split('-'))


class TomorrowGames:
    WEB_LINKS = {
        "today": 'https://www.oddsportal.com/matches/',
        "yesterday": 'https://www.oddsportal.com/matches/soccer/' + get_yesterday_date(),
    }

    REGEX = {
        "score": r'[t][a][b][l][e]\-[s][c][o][r][e]\"\>(\d{1,2}\:\d{1,2})\<\/',
        "both_teams_draw": r'\/\"\>([A-z0-9].{1,40})[ ]\-[ ]([A-z0-9].{1,40})\<\/[a]',
        "home_won": r'[s][p][a][n][ ][c][l][a][s][s]\=\"[b][o][l][d]\"\>([A-z0-9].{1,40})\<\/[s][p][a][n]',
        "home_loosing": r'\/\"\>([A-z0-9].{1,40})[ ]\-[ ]',
        "away_winning": r'[c][l][a][s][s]\=\"[b][o][l][d]\"\>([A-z0-9].{1,40})\<\/[s][p]',
        "away_loosing": r'\<\/[s][p][a][n]\>[ ]\-[ ]([A-z0-9].{1,40})\<\/[a]',
        "time": r'[0]\"\>(\d{1,2}[:]\d{1,2})\<\/[t][d]',
        "odds": r'(\"\>|\=\")(\d{1,2}[.]\d{1,2})(\<\/[a]|\"[ ])',
        "result": r'([c][o][r][e]\"\>(\d{1,2}[:]\d{1,2})([ ][p][e][n]|\<\/[t][d])|[p][o][s][t][p])'
    }

    def scrape(self):
        for link in self.WEB_LINKS.keys():
            # OPEN THE BROWSER
            driver = self.open_the_browser(link)

            # GET THE DATA
            all_games = self.get_the_data(driver)

            # CLEAN DATA
            self.clean_data(all_games)

    def open_the_browser(self, link):
        # OPEN THE BROWSER
        options = ChromeOptions()
        options.headless = True  # IF YOU WANT TO SEE THE BROWSER -> FALSE
        driver = Chrome(options=options, executable_path=ChromeDriverManager().install())
        driver.get(self.WEB_LINKS[link])
        sleep(4)
        return driver

    def get_the_data(self, driver):
        # GET THE DATA
        html = driver.execute_script('return document.documentElement.outerHTML;')
        soup = BeautifulSoup(html, 'html.parser')
        driver.close()
        games = soup.find_all('tr')
        return games

    def clean_data(self, games):
        # CLEAN THE DATA
        the_bulk = []
        scores = []
        for game in games:
            # print(game)
            score = re.search(self.REGEX['score'], str(game))
            try:
                if score:
                    score = score.group(1)
                    [home_score, away_score] = score.split(':')
                    home_team, away_team = '', ''

                    if home_score > away_score:
                        home_team = re.search(self.REGEX['home_won'], str(game)).group(1)
                        away_team = re.search(self.REGEX['away_loosing'], str(game)).group(1)
                        print(f'{home_team} {score} {away_team}')
                    elif home_score == away_score:
                        tokens = re.search(self.REGEX['both_teams_draw'], str(game))
                        home_team, away_team = tokens.group(1), tokens.group(2)
                        print(f'{home_team} {score} {away_team}')
                    else:
                        home_team = re.search(self.REGEX['home_loosing'], str(game)).group(1)
                        away_team = re.search(self.REGEX['away_winning'], str(game)).group(1)
                        print(f'{home_team} {score} {away_team}')

                    qset = RegularGame.objects.filter(home_team=home_team, away_team=away_team)
                    szd_qset = json.loads(serializers.serialize('json', qset))[0]

                    res_game = ResultGame(pk=szd_qset['pk'], time=szd_qset['fields']['time'], home_team=szd_qset['fields']['home_team'],
                                          away_team=szd_qset['fields']['away_team'], score=score,
                                          home_odd=szd_qset['fields']['home_odd'],
                                          draw_odd=szd_qset['fields']['draw_odd'],
                                          away_odd=szd_qset['fields']['away_odd'])

                    if not ResultGame.objects.filter(pk=szd_qset['pk']).exists():
                        print('NQMAME')
                        the_bulk.append(res_game)
                    print(res_game)

            except Exception as e:
                print(e)

        print(the_bulk)
        ResultGame.objects.bulk_create(the_bulk)


# if __name__ == '__main__':
#     tmr = TomorrowGames()
#     tmr.scrape()
