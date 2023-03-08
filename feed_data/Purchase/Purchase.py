import requests
import config

def buy(url):
  r = requests.post(config.purchase_server + "/purchase", 
    data={
      'url': url
    })
  print(r.status_code)
  print(r.text)
  return r.text
      
