import reqDataPOST
#This script will give information about game
class GameInformation:
    def __init__(self,game):
        self.game=game
        soup=reqDataPOST.POSTReq(f"{game}").returnAllData
        self.gameInfoSnippet = soup.select(".game_description_snippet")[0].text
        self.gameReview=soup.find('div', attrs = {'class':"summary column"}).text
        self.allGameReviews=soup.select("#userReviews > div:nth-child(2) > div:nth-child(2)")[0].text
        self.developer=soup.select("#developers_list > a:nth-child(1)")[0].text
        self.publisher=soup.select("div.dev_row:nth-child(4) > div:nth-child(2) > a:nth-child(1)")[0].text
        self.sysreq=soup.select(".sysreq_contents")[0].text
        self.date=soup.select(".date")[0].text
        self.langs=soup.select("div.block:nth-child(9)")[0].text
        self.gameCategory=soup.select("#category_block")[0].text
        self.aboutGame=soup.select("#aboutThisGame")[0].text
        self.gameVideo = soup.find('div', attrs = {'class':'highlight_player_item highlight_movie'}).get("data-mp4-hd-source")
        self.gameImages = soup.find_all('div', attrs = {'class':'highlight_strip_item highlight_strip_screenshot'})
    @property
    def returnAvailableLangs(self):
        self.languages=set()
        translator = str.maketrans({chr(9): '', chr(9): ''})
        for i in self.langs.translate(translator).split("\n"):
            if i!="" and i!="\r" and i!="✔":
                self.languages.add(i)
        return self.languages
    @property
    def returnImages116x65(self):
        self.imageLinks_=set()
        for i in self.gameImages:
            self.imageLinks_.add(i.find("img").get("src"))
        return self.imageLinks_
    @property
    def returnImages600x338(self):
        self.imageLinks=set()
        for i in self.gameImages:
            self.imageLinks.add(i.find("img").get("src").replace("116x65.jpg","600x338.jpg"))
        return self.imageLinks
    @property
    def returnGameVideo(self):
        return self.gameVideo.strip()
    @property
    def returnGameCategory(self):
        return self.gameCategory.strip()
    @property
    def returnInfoSnippet(self):
        return self.gameInfoSnippet.strip()
    @property
    def returnRecentGameReview(self):
        translator = str.maketrans({chr(10): '', chr(9): ''})
        return self.gameReview.translate(translator)
    @property
    def returnAllGameReviews(self):
        translator = str.maketrans({chr(10): '', chr(9): ''})
        return self.allGameReviews.translate(translator)
    @property
    def returnDate(self):
        return self.date.strip()
    @property
    def returnSysReq(self):
        return self.sysreq.strip()
    @property
    def returnAboutGame(self):
        return self.aboutGame.strip()
"""
print(GameInformation("gta5").returnGameVideo)
print(GameInformation("gta5").returnImages600x338)
print(GameInformation("gta5").returnImages116x65)
print(GameInformation("gta5").returnGameCategory)
print(GameInformation("gta5").returnInfoSnippet)
print(GameInformation("gta5").returnAvailableLangs)
print(GameInformation("gta5").returnDate)   
print(GameInformation("gta5").returnSysReq) 
print(GameInformation("gta5").returnAllGameReviews)
print(GameInformation("gta5").returnRecentGameReview)"""

