import webbrowser
import pyautogui as ctr
import os, time, keyboard
from datetime import datetime
import common.utils as utils
import subprocess

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

class ChromePurchase:
  
  
  def __init__(self):
    self.browser = webbrowser.get('open -a /Applications/Google\ Chrome.app %s')
    self.image_path = ROOT_DIR + '/images/chrome/limin/'

  def addToShoppingCard(self, url):
    message = ""
    self.wakeup_machine()
    time.sleep(10)
    print("START - Buying process")
    print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    print(f'url: {url}')
    self.browser.open(url)
    ctr.moveTo(10,110, duration =2)
    utils.findAndClick(self.image_path + 'user_icon.png', isDoubleClick = True)

    position = utils.findAndClick(self.image_path + 'login_button.png', y_adj = -20, isDoubleClick = True)

    if position is None:
      utils.findAndClick(self.image_path + 'home_icon.png', isDoubleClick = True) 
    else:
      position = utils.findAndClick(self.image_path + 'continue_shopping_button.png', isDoubleClick = True)
      if position is None:
        utils.findAndClick(self.image_path + 'home_icon.png', isDoubleClick = True) 
    

    utils.findAndClick(self.image_path + 'add_to_cart_button.png', isDoubleClick = True)

    position = utils.findAndClick(self.image_path + 'bag_not_enable.png')
    
    
    # if click add to cart button and find not available button, stop rest process
    if position is not None:
      message = "not_available"
      print("Bag is not available")
    else: 
      utils.findAndClick(self.image_path + 'cart_button.png', isDoubleClick = True)
      utils.findAndClick(self.image_path + 'confirm_1_in_cart_button.png', isDoubleClick = True)
      message = "available"
      
      # utils.keepForceOnBrowser()
      # ctr.scroll(-200)
      # time.sleep(2)

      # position = utils.findAndClick(self.image_path + 'confirm_2_delivery_button.png', isDoubleClick = True)
      # if position is None:
      #   position = utils.findAndClick(self.image_path + 'confirm_1_a_user_name_fields_button.png')
      #   time.sleep(3)
      #   position = utils.findAndClick(self.image_path + 'confirm_1_a_user_name_fields_button.png')
      #   time.sleep(3)
      #   position = utils.findAndClick(self.image_path + 'confirm_2_delivery_button.png', isDoubleClick = True)

      # ctr.scroll(-500)
      # time.sleep(1)

      # utils.findAndClick(self.image_path + 'confirm_3_card_code.png', isDoubleClick = True)
      # keyboard.write("283")
      # utils.keepForceOnBrowser()
      # position = utils.findAndMouseDown(self.image_path + 'confirm_4_term_check.png')
      # if position is not None:
      #   ctr.click()

      # real to buy, BE CAREFUL
      # utils.findAndClick(self.image_path + 'confirm_5_buy_button.png', isDoubleClick = True)

    print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    print("COMPLETE - Buying process")
    print("")
    print("")
    return message

  def wakeup_machine(self):
    print("Wake up server machine")
    subprocess.Popen('cd /Users/limin/Documents/yspace && sudo ./wakeup.sh',
                        shell=True, stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
