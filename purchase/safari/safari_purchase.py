import webbrowser
import pyautogui as ctr
import os, time, keyboard
import common.utils as utils

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

class SafariPurchase:
  
  
  def __init__(self):
    self.browser = webbrowser.get('open -a /Applications/Safari.app %s')
    self.image_path = ROOT_DIR + '/images/safari/'

  def addToShoppingCard(self, url):
    print(f'url: {url}')
    self.browser.open(url)
    time.sleep(4)
    utils.findAndClick(self.image_path + 'user_icon.png')

    time.sleep(4)
    position = utils.findAndClick(self.image_path + 'user_email_field.png')
    if position is not None:
      keyboard.write("yimingliu0216@gmail.com")

    time.sleep(4)
    position = utils.findAndClick(self.image_path + 'user_password_field.png')
    if position is not None:
      keyboard.write("Cc00114110!")

    time.sleep(4)
    position = utils.findAndClick(self.image_path + 'login_button.png')

    time.sleep(4)
    position = utils.findAndClick(self.image_path + 'continue_shopping_button.png')

  