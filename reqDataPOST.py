import requests
from bs4 import BeautifulSoup
import _search_
#This script will make a post request(used in age verification)
class POSTReq:
    def __init__(self,game):
        game=_search_.Game(game)
        headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"
        }
        cookies={
            "birthtime":"975704401",
            "browserid":"5045749419015102585",
            "lastagecheckage":"2-0-2001",
            "sessionid":"57509a8a12bed62072935e24",
            "steamCountry":"TR|a6b9bd9d58c098bac19c3f0c3913e603",
            "timezoneOffset":"10800,0"
        }
        self.data=requests.post(f"{game}",headers=headers,cookies=cookies)
        self.soup = BeautifulSoup(self.data.content,"lxml")
        self.result = self.soup.find('div', attrs = {'id':'recommended_block'}).find('a',attrs={'class':'deck_view_all_action_link'}).get("href")
    @property
    def returnSimilarGames(self):
        return self.result
    @property
    def returnAllData(self):
        return self.soup
