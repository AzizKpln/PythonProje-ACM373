import requests
from bs4 import BeautifulSoup
import _search_
#This script will make a GET request(used in standard requests)
class GETReq:
    def __init__(self,game):
        game=_search_.Game(game)
        headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"
        }
        data=requests.post(f"{game}",headers=headers)
        soup = BeautifulSoup(data.content,"lxml")
        self.result = soup.find('div', attrs = {'id':'recommended_block'}).find('a',attrs={'class':'deck_view_all_action_link'}).get("href")
    def __str__(self):
        return self.result
