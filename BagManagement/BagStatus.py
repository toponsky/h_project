import requests
from bs4 import BeautifulSoup as BS
from requests_html import HTMLSession
import config
import time
import random

from ProxyManagement import ProxyManager
from EmailManagement import EmailManager

class BagStatus:
  
  def __init__(self, db, proxy_manager, email_agent):
    self.db = db
    self.proxyMger = proxy_manager
    self.email = email_agent

  def checkAvailable(self):    
    #for bag in self.db.getBags():
     # self.proxyMger.startNextProxy()
     # time.sleep(random.randint(10,15))  
      #if self.updateBag(bag):  
     #   break;
    #  time.sleep(random.randint(10,20))  

    self.updateBag(self.db.getBags()[0])  
    
            

  def updateBag(self, bag):
    url = config.BASE_URL + bag.get('url')
    _id = bag.get('_id')
    session = HTMLSession()
    isBlocked = False
    try:
      response = session.get(url, headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
      colorSections = len(response.html.find('h-product-variants'))
      blockerDiv = len(response.html.find('#cmsg'))
      print('Url: {0}'.format(url))
      print(response.content)
      if blockerDiv > 0:
        print('bag website is blocked')
        self.db.updateBagStatus(_id, isBlocked = True)
        isBlocked = True

      elif colorSections == 0:
        print('bag NOT enable')
        self.db.updateBagStatus(_id, isAvailable = False)

      elif colorSections > 0:
        print('bag enable')
        self.db.updateBagStatus(_id, colorSection = colorSections)
        self.email.sendBag(bag)
      
      elif hasattr(response.html.find('h1', first=True), 'text') and response.html.find('h1', first=True).text == 'Verflixtes Internet!':
        print('bag website destroyed')
        self.db.updateBagStatus(_id, isDestroy = True)
        
    
    except requests.exceptions.RequestException as e:
      print(e)

    return isBlocked
