import requests
from bs4 import BeautifulSoup as BS
import config

class BagInfo:
  def __init__(self, db, urls):
    self.db = db
    self.urls = urls

  def collectBagsInfo(self):
    for country in self.urls:
        self.soupify(self.urls[country])

  def soupify(self, url):
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
    # content = open('Output.txt', 'r').read()
    soup = BS(page.text, 'html.parser')
    
    allBags = soup.find_all('div', {'product-grid-list-item'})
    length = len(allBags)
    i=0
    for bag in allBags:
        b= allBags[i]
        href = b.find('a')
        img  = b.find('img')
        text = b.text.split(',')
        
        p_id = href.get('id')
        if not self.db.isBagExists(p_id):
          p_url = href.get('href')
          p_img_url = img.get('src')
          p_name = text[0]
          p_color = text[1].split(':')[1].replace('\xa0 ','').strip()
          p_price = text[2].replace('\xa0 ','').replace(' €\n', '')
          self.db.insertOneBag(p_id,p_url,p_img_url,p_name,p_color,p_price)
          print('{0}.{1}'.format(i, b.text))
        i +=1  