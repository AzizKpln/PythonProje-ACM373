import requests
from bs4 import BeautifulSoup
#This script will search for a spesific game
class Game:
    def __init__(self,game):
        headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"
        }
        data=requests.get(f"https://store.steampowered.com/search/?term={game}",headers=headers)
        soup = BeautifulSoup(data.content,"lxml")
        self.result = soup.select('a.search_result_row:nth-child(1)')[0].get("href")
    def __str__(self):
        return self.result