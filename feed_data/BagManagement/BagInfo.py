import requests
import time
from bs4 import BeautifulSoup as BS
import config

class BagInfo:
  def __init__(self, db, email, urls):
    self.db = db
    self.urls = urls
    self.email = email

  def collectBagsInfo(self):
    for country in self.urls:
        self.soupify(self.urls[country])

  def soupify(self, url):
    print("URL: {0}".format(url))
    start_time = time.time()
    collectLog = {}
    proxy = "http://458be2d6aa1638f2627cec41c06494e314ae0b40:js_render=true&antibot=true&premium_proxy=true&proxy_country=de@proxy.zenrows.com:8001"
    proxies = {"http": proxy, "https": proxy}
    collectLog['url'] = url
    response = requests.get(url, proxies=proxies, verify=False)
    isSuccess = response.ok
    collectLog['response_status'] = isSuccess
    if isSuccess:
      soup = BS(response.text, 'html.parser')
      allBags = soup.find_all('div', {'product-grid-list-item'})
      length = len(allBags)
      i=0
      add_index = 0;
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
            self.db.insertEmailLog(self.email.sendNewBagRawData(self.db.getEmailAddresses(), p_url, p_img_url, p_name, p_color)) 
            print('{0}.{1}'.format(i, b.text))
            add_index = add_index + 1
          i +=1     
      collectLog['amount'] = add_index
    else:
      collectLog['err_code'] = response.status_code
      if response.status_code == 422:
          isSuccess = False  
          err_msg = json.loads(response.text)['title']
          collectLog['err_msg'] = err_msg

    collectLog['render_time'] = int((time.time() - start_time))
    self.db.insertCollectLog(collectLog)