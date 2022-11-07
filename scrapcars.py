from bs4 import BeautifulSoup
from requests import get
import pandas as pd


URL= "https://www.otomoto.pl/osobowe/audi"


page = get(URL)
websitecontent = BeautifulSoup(page.content, "html.parser")


for offers in websitecontent.find_all("article" , class_="ooa-15j3s1f e1b25f6f0"):
    nazwa = offers.find("h2", class_="e1b25f6f6 e1b25f6f19 ooa-10p8u4x er34gjf0").get_text()
    miasto = offers.find ("span", class_="ooa-fzu03x").get_text()
    scrapthislater = offers.find("ul").get_text() #split it to 3 elements
    price = offers.find ("span", class_="ooa-1bmnxg7 e1b25f6f11").get_text()
    
    
    things= [nazwa,miasto,scrapthislater, price]
    print (things)
