import requests

def buy(url):
  r = requests.post("http://192.168.178.68:5000/purchase", 
    data={
      'url': url
    })
  print(r.status_code)
  print(r.text)
      
