from bs4 import BeautifulSoup
from requests import get
import pandas as pd

allcars= list()
cols = ['model', 'city', 'productionyear','milage','engine', 'price']
for x in range(1,500):
    
    URL= "https://www.otomoto.pl/osobowe/audi?page="+str(x)
    print (x)

    page = get(URL)
    websitecontent = BeautifulSoup(page.content, "html.parser")


    for offers in websitecontent.find_all("article" , class_="ooa-15j3s1f e1b25f6f0"):
        carelems = list()
        model = offers.find("h2", class_="e1b25f6f6 e1b25f6f19 ooa-10p8u4x er34gjf0").get_text()
        city = offers.find ("span", class_="ooa-fzu03x").get_text()
        scrapthislater = offers.find("ul")
        for li in scrapthislater.findAll('li'):
            carelems.append(li.get_text())
        
        price = offers.find ("span", class_="ooa-1bmnxg7 e1b25f6f11").get_text()
        
        if (len(carelems)==4):
            productionyear = carelems[0]
            milage= carelems[1]
            engine=carelems[2]
        
        things= [model,city,productionyear,milage,engine, price]
        allcars.append(things)
cardata = pd.DataFrame(allcars,columns = cols)
cardata.to_csv('carzall.csv',encoding='utf-16')
