import requests
from bs4 import BeautifulSoup as BS
from requests_html import HTMLSession

class BagStatus:
  
  def __init__(self, db):
    self.BASE_URL='https://www.hermes.com'
    self.db = db


  def checkAvailable(self):
    bags = self.db.getBags()

    for bag in self.db.getBags():
      if self.updateBag(bag):
        break
      

  def updateBag(self, bag):
    url = self.BASE_URL + bag.get('url')
    _id = bag.get('_id')
    session = HTMLSession()
    isBlocked = False
    try:
      
      response = session.get(url, headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
      cart_button =  response.html.find("button[name=add-to-cart]")
      message = response.html.find('span[class=message-info]')
      h1_div = response.html.find('h1', first=True)

      if len(message) == 1:
        print('bag NOT enable')
        self.db.updateBagStatus(_id, isAvailable = False)

      elif len(message) == 0 and len(cart_button) > 1:
        print('bag enable')
        colorSections = len(response.html.find('h-product-variants'))
        self.db.updateBagStatus(_id, color_section = colorSections)
      elif hasattr(response.html.find('h1', first=True), 'text') and response.html.find('h1', first=True).text == 'Verflixtes Internet!':
        print('bag website destroyed')
        self.db.updateBagStatus(_id, isDestroy = True)
      else:
        print('bag website is blocked')
        self.db.updateBagStatus(_id, isBlocked = True)
        isBlocked = True
    
    except requests.exceptions.RequestException as e:
      print(e)

    return isBlocked