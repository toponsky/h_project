import requests
from bs4 import BeautifulSoup as BS
import config
import time
import json

from ProxyManagement import ProxyManager
from EmailManagement import EmailManager
from SMSManangement import SMSManager

class BagStatus:
  
  def __init__(self, db, email_agent):
    self.db = db
    self.email = email_agent
    requests.packages.urllib3.disable_warnings()

  def checkAvailable(self):
    requestLog = {}
    start_time = time.time()
    failList = []
    amount, bags = self.db.getBagRequestList()
    
    self.db.insertResponseLog({
      "comment": "Start Check Bags"
    })
    for bag in bags:
      if not self.updateBag(bag):
        failList.append(bag)
    
    self.db.insertResponseLog({
      "fail_no": len(failList),
      "comment": "Try second time, With '{0}'s fails".format(len(failList))
    })
    # Try second fail check   
    for bag in failList:
      self.updateBag(bag)

    if len(failList) == 0:
      msg = "COMPLETE list" 
    else: 
      msg = "{0} number bags fail".format(len(failList))

    
    self.db.insertResponseLog({
      'check_no': amount,
      "fail_no": len(failList),
      "comment": "Finish Check Bags, With : '{0}' and took {1}s".format(msg, int(time.time() - start_time))
    })


  def updateBag(self, bag):
    start_time = time.time()
    requestLog = {}
    url = config.BASE_URL + bag.get('url')
    proxy = "http://458be2d6aa1638f2627cec41c06494e314ae0b40:js_render=true&antibot=true&premium_proxy=true&proxy_country=de@proxy.zenrows.com:8001"
    proxies = {"http": proxy, "https": proxy}
    b_id = bag.get('id')
    isSuccess = False
    print("URL: {0}".format(url))
    requestLog['url'] = url
    try:    
      response = requests.get(url, proxies=proxies, verify=False)      
      isSuccess = response.ok
      requestLog['response_status'] = isSuccess
      print("Get Response '{0}'".format(isSuccess))
      if isSuccess:
        soup = BS(response.text, 'html.parser')

        colorSections = len(soup.find_all("h-product-variants"))
        blockerDiv = len(soup.find_all("div", {"id": "cmsg"}))
        
        
        if blockerDiv > 0:
          print('BAG WEBSITE IS BLOCKED')
          requestLog['bag_status'] = 'BAG WEBSITE IS BLOCKED'
          self.db.updateBagStatus(b_id, isBlocked = True)
          isBlocked = True

        elif colorSections == 0:
          requestLog['bag_status'] = 'BAG NOT ENABLE'
          print('BAG NOT ENABLE')
          self.db.updateBagStatus(b_id, isAvailable = False)

        else:
          requestLog['bag_status'] = 'BAG ENABLE'
          print('BAG ENABLE ....')
          self.db.updateBagStatus(b_id, colorSection = colorSections)
          self.db.insertEmailLog(self.email.sendBag(self.db.getEmailAddresses(), bag)) 
          self.db.insertSMSLog(SMSManager.sendBagSMS(self.db.getSMSNumbers(), bag.get('name'))) 
      else:
        requestLog['err_code'] = response.status_code 
        print('Fail code: {0}'.format(response.status_code))  
        if response.status_code == 404:
          self.db.updateBagStatus(b_id, isDestroy = True)
          isSuccess = True
          requestLog['err_msg'] = 'bag website is destroyed'
          print('bag website is destroyed')  

        elif response.status_code == 422:
          isSuccess = False  
          err_msg = json.loads(response.text)['title']
          requestLog['err_msg'] = err_msg
          print('Fail detail: {0}'.format(err_msg))

        elif response.status_code == 403:
          isSuccess = True
          requestLog['err_msg'] = 'No credit in account, please topup'
          print('No credit in account, please topup')
      
      
  
    except requests.exceptions.RequestException as e:
      print(e)

    print("")
    print("")
    requestLog['render_time'] = (time.time() - start_time)
    self.db.insertResponseLog(requestLog)
    return isSuccess

    
