import requests
from bs4 import BeautifulSoup as BS
from requests_html import HTMLSession
import config
import time
import random
from pathlib import Path

from ProxyManagement import ProxyManager
from EmailManagement import EmailManager

class BagStatus:
  
  def __init__(self, db, email_agent):
    self.db = db
    self.email = email_agent

  def checkAvailable(self):    
    for bag in self.db.getBagRequestList():
      self.updateBag(bag)
     # self.proxyMger.startNextProxy()
     # time.sleep(random.randint(10,15))  
      #if self.updateBag(bag):  
     #   break;
    #  time.sleep(random.randint(10,20))  
      
    
            

  def updateBag(self, bag):
    url = config.BASE_URL + bag.get('url')
    proxy = "http://458be2d6aa1638f2627cec41c06494e314ae0b40:js_render=true&antibot=true&premium_proxy=true&proxy_country=de@proxy.zenrows.com:8001"
    proxies = {"http": proxy, "https": proxy}
    _id = bag.get('_id')
    print("Start URL {0}".format(url))
    try:  
      
      response = requests.get(url, proxies=proxies, verify=False)
      import pdb; pdb.set_trace()
      print(response.content)
      soup = BS(response.text, 'html.parser')

      # text = Path('tmp.html').read_text()
      # soup = BS(text, 'html.parser')

      colorSections = len(soup.find_all("h-product-variants"))
      blockerDiv = len(soup.find_all("div", {"id": "cmsg"}))
      
      
      if blockerDiv > 0:
        print('bag website is blocked')
        self.db.updateBagStatus(_id, isBlocked = True)
        isBlocked = True

      elif colorSections == 0:
        print('bag NOT enable')
        self.db.updateBagStatus(_id, isAvailable = False)

      else:
        print('bag enable')
        self.db.updateBagStatus(_id, colorSection = colorSections)
        self.email.sendBag(bag)
        
    
    except requests.exceptions.RequestException as e:
      import pdb; pdb.set_trace()
      print(e)
      
