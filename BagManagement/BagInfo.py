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
    response = requests.get("https://api.zenrows.com/v1/?apikey=458be2d6aa1638f2627cec41c06494e314ae0b40&url=https%3A%2F%2Fwww.hermes.com%2Fde%2Fde%2Fcategory%2Fdamen%2Ftaschen-und-kleinlederwaren%2Ftaschen-und-kleine-taschen%2F&js_render=true&antibot=true&premium_proxy=true", verify=False)

    print(response.content)
    soup = BS(response.text, 'html.parser')
    
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