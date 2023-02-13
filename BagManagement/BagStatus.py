import requests
from bs4 import BeautifulSoup as BS

class BagStatus:
  
  def __init__(self, db):
    self.BASE_URL='https://www.hermes.com'
    self.db = db


  def checkAvailable(self):
    bags = self.db.getBags()

    # for bag in self.db.getBags():
    #   url = self.BASE_URL + bag.get('url')
    url = "https://www.hermes.com/de/de/product/tasche-steeple-25-H083618CKAB/"
    self.updateBag(url)
    print(url)
    
      

  def updateBag(self, url):
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
    with open("my_file.txt", "a") as f:
      f.write(page.text)

    