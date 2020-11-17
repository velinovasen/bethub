import sys, os, django
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

from traffic.models import RegularGame

def get_tomorrow_date(token):
    datetime.today().strftime('%Y-%m-%d')
    tomorrow_date = (datetime.today() + timedelta(hours=24)).strftime('%Y-%m-%d')
    if token == 'link':
        return "".join(tomorrow_date.split('-'))
    return "-".join(tomorrow_date.split('-'))


class TomorrowGames:

    WEB_LINKS = {
        "today_oddsportal": 'https://www.oddsportal.com/matches/',
        "oddsportal": 'https://www.oddsportal.com/matches/soccer/' + get_tomorrow_date('link')
    }

    REGEX = {
        "score": r'([t][a][b][l][e]\-[s][c][o][r][e]\"\>|[i][n]\-[p][l][a][y][ ][o][d][d][s])',
        "home_away_scheduled": r'(\/\"\>([A-z0-9].+)[ ]\-|[d]\"\>([A-z0-9].+)\<\/[s][p][a])[ ]([A-z0-9].{1,40})\<\/[a]',
        "time": r'[0]\"\>(\d{1,2}[:]\d{1,2})\<\/[t][d]',
        "odds": r'(\"\>|\=\")(\d{1,2}[.]\d{1,2})(\<\/[a]|\"[ ])',
        "result": r'([c][o][r][e]\"\>(\d{1,2}[:]\d{1,2})([ ][p][e][n]|\<\/[t][d])|[p][o][s][t][p])'
    }

    def scrape(self):
        RegularGame.objects.all().delete()
        for link in self.WEB_LINKS.keys():
            # OPEN THE BROWSER
            driver = self.open_the_browser(link)

            # GET THE DATA
            all_games = self.get_the_data(driver)

            # CLEAN DATA
            self.clean_data(all_games, link)

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

    def clean_data(self, games, link):
        # CLEAN THE DATA
        the_bulk = []
        for game in games:
            # FIND THE TIME
            score = re.search(self.REGEX['score'], str(game))
            if not score:
                try:
                    both_teams = re.search(self.REGEX["home_away_scheduled"], str(game))
                    home_team = str(both_teams.group(2))
                    away_team = str(both_teams.group(4))
                    if '&amp;' in home_team:
                        home_team = home_team.replace('&amp;', 'n')
                    if '&amp;' in away_team:
                        away_team = away_team.replace('&amp;', 'n')
                    if 'Group' in away_team or 'III' in home_team or 'PFL' in home_team:
                        continue
                    else:
                        time = re.search(self.REGEX["time"], str(game)).group(1)
                        if link == 'oddsportal':
                            time += ' ' + get_tomorrow_date('not link')
                        home_odd, draw_odd, away_odd = '', '', ''
                        try:
                            odds = re.findall(self.REGEX["odds"], str(game))
                            [home_odd, draw_odd, away_odd] = [odds[0][1], odds[2][1], odds[3][1]]

                        except IndexError:
                            continue

                        except ValueError:
                            print('Most likely, we got missing odds')

                        the_bulk.append(RegularGame(time=time, home_team=home_team, away_team=away_team,
                                                    home_odd=home_odd, draw_odd=draw_odd, away_odd=away_odd))
                except AttributeError:
                    continue

        RegularGame.objects.bulk_create(the_bulk)


if __name__ == '__main__':
    tmr = TomorrowGames()
    tmr.scrape()
