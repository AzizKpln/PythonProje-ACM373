import requests
from bs4 import BeautifulSoup
import os
import reqDataPOST
import json
#This script will retrieve the similar games related with the given game
class similarGames:
    def __init__(self,gameLink,img):
        x=1
        self.gameLink=gameLink
        self.imageLinks=list()
        self.listOFGames=list()
        self.listOFPrices=list()
        self.gameAndPrice=dict()
        self.headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"
        }
        data=requests.get(f"{self.gameLink}",headers=self.headers)
        soup = BeautifulSoup(data.content,"lxml")
        while True:
            try:
                if img==False:
                    #we get the link of games if the img variable equals to False
                    self.link_ = soup.select(f'#released > div:nth-child({x}) > div:nth-child(1) > a:nth-child(1)')[0].get("href")
                    self.returnGames=self.link_
                elif img==True:
                    #we get the link of images if the img variable equals to True
                    self.link_ = soup.select(f'#released > div:nth-child({x}) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)')[0].get("srcset")
                    self.imageLinks.append(self.link_)
                self.price_ = soup.select(f'#released > div:nth-child({x}) > div:nth-child(2) > div:nth-child(1)')[0].text
                
                self.returnPrice=self.price_
                self.gameAndPrice[self.link_]=self.price_.strip()
                x+=1
            except IndexError:
                break

    """
    //this algorithm has to change. No need for local installation
    @property
    def downloadImages(self):
        x=0
        f = open('ImageID_Data/ImageID.json');self.ImageID = json.load(f);f.close()
        NewImageID = {"ImageID":int(self.ImageID["ImageID"])+1}
        os.system("mkdir ImageID"+str(self.ImageID["ImageID"]))
        for i in self.returnGames:
            data=requests.get(i,headers=self.headers)
            with open("ImageID"+str(self.ImageID["ImageID"])+f"/Image{x}.png","wb") as byteCode:
                byteCode.write(data.content)
                x+=1
        with open("ImageID_Data/ImageID.json","w",encoding="utf-8") as ImageID:
            ImageID.write(json.dumps(NewImageID))"""
    #special decorator for returning data
    @property
    def getImageLinks(self):
        #more accurate algorithm for getting the links
        return self.imageLinks
    @getImageLinks.setter
    def getImageLinks(self,val):
        #more accurate algorithm for getting the links
        self.imageLinks.append(val)
        
        
        
    @property
    def returnPriceAndGames(self):
        return self.gameAndPrice
    @property
    def returnPrice(self):
        return self.listOFPrices
    @returnPrice.setter
    def returnPrice(self,val):
        self.listOFPrices.append(val)
    @property
    def returnGames(self):
        return self.listOFGames
    @returnGames.setter
    def returnGames(self,val):
        self.listOFGames.append(val)

#print(similarGames(str(reqDataPOST.POSTReq("gta5").returnSimilarGames),True).downloadImages())
#print(similarGames(str(reqDataPOST.POSTReq("gta5").returnSimilarGames),False).returnGames)
# to get the links and prices print(similarGames("https://store.steampowered.com/recommended/morelike/app/351920/",False).returnPriceAndGames)
# to get links we use similarGames(str(reqDataPOST.POSTReq("gta5"),True).returnGames
# to get images we use similarGames(str(reqDataPOST.POSTReq("gta5"),True).downloadImages()
    