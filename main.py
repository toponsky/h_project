from bs4 import BeautifulSoup as BS
from lxml import html
import requests
import config
from DBManagement import Database as Database

def soupify(url, bags, db):
    # page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'},verify=False, proxies=proxy)
    # soup = BS(page.text, 'lxml')

    # # allbags = soup.find_all('h3', {'class':'product-item-name'})
    # allBags = soup.find_all('div', {'product-grid-list-item'})
    # import pdb; pdb.set_trace()
    # for b in allBags:
    #     print(b.text)

    db.insertOneBag("p_id", "name", "imageURL", "url")
    print("I am here")

if __name__ == "__main__":
             
    db = Database.Database(config.db_connection["username"], config.db_connection["password"])
    for country in config.urls:
        soupify(config.urls[country], config.bag_names, db)
      