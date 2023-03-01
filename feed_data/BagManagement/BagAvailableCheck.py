import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime
import config
import time
import json

from ProxyManagement import ProxyManager
from EmailManagement import EmailManager
from SMSManangement import SMSManager

class BagAvailableCheck:
  
  def __init__(self, db):
    self.db = db
    requests.packages.urllib3.disable_warnings()

  def checkAvailable(self):
    requestLog = {}
    start_time = time.time()
    failList = []
    amount, bags = self.db.getAllBags()

    self.db.insertAavaiableCheckLog({
      "comment": "Start Bags Avaiable Check"
    })
    for bag in bags:
      if not self.updateBag(bag):
        failList.append(bag)
    
    self.db.insertAavaiableCheckLog({
      "fail_no": len(failList),
      "comment": "Try second time, With '{0}'s fails".format(len(failList))
    })
    s_index = 0
    # Try second fail check   
    for bag in failList:
      if self.updateBag(bag):
        s_index =s_index + 1
      
    fail_no = len(failList) - s_index
    if fail_no == 0:
      msg = "COMPLETE list" 
    else: 
      msg = "{0} number bags fail".format(fail_no)

    
    self.db.insertAavaiableCheckLog({
      'check_no': amount,
      "fail_no": len(failList) - s_index,
      "comment": "Finish Bags avaiable Check, With : '{0}' and took {1}s".format(msg, int(time.time() - start_time))
    })


  def updateBag(self, bag):
    start_time = time.time()
    requestLog = {}
    url = config.BASE_URL + bag.get('url')
    proxy = "http://458be2d6aa1638f2627cec41c06494e314ae0b40:js_render=true&antibot=true&premium_proxy=true&proxy_country=de@proxy.zenrows.com:8001"
    proxies = {"http": proxy, "https": proxy}
    b_id = bag.get('id')
    isSuccess = False
    print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    print("URL: {0}".format(url))
    requestLog['url'] = url
    try:    
      response = requests.get(url, proxies=proxies, verify=False)      
      isSuccess = response.ok
      requestLog['response_status'] = isSuccess
      print("Get Response '{0}'".format(isSuccess))
      if isSuccess:
        self.db.updateBagStatus(b_id, isAvailable=bag.get('is_available'), colorSection=bag.get('color_section')) 
        print('Website for Bag: "{0}"  ----> is avaiable'.format(bag.get('name')))
        requestLog['bag_website']= 'Available'
      else:
        requestLog['err_code'] = response.status_code 
        print('Fail code: {0}'.format(response.status_code))  
        if response.status_code == 404:
          self.db.updateBagStatus(b_id, isDestroy = True)
          isSuccess = True
          requestLog['bag_website'] = 'Not Available'
          print('Website for Bag: "{0}" ----> is NOT avaiable'.format(bag.get('name')))

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
    requestLog['render_time'] =int((time.time() - start_time))
    self.db.insertAavaiableCheckLog(requestLog)
    return isSuccess

    
