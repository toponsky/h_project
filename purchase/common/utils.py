import pyautogui as ctr
import time

def get_position(image: str, waiting = 4,  y_adj = 0):
  try:
    time.sleep(waiting)
    position = ctr.locateCenterOnScreen(image, confidence = 0.7)
    if position is None:
      print(f'{image} not found on screen')
      return None
    else:
      print("action image: " + image)
      x = position.x
      y = position.y
      return x, y - y_adj

  except OSError as e:
    raise Exception(e)
    return None


def findAndClick(url, y_adj = 0, isDoubleClick = False):
  position = get_position(url, y_adj = y_adj)
  print(position)
  if position is not None:
    ctr.moveTo(position, duration = 1)
    ctr.click()
    if isDoubleClick:
      ctr.click()

  return position 


def findAndMouseDown(url, y_adj = 0):
  position = get_position(url, y_adj = y_adj)
  print(position)
  if position is not None:
    ctr.moveTo(position, duration = 1)
    ctr.mouseDown()
  return position      


def keepForceOnBrowser():
  ctr.moveTo(80, 500)
  ctr.click()  


