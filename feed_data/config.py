import requests

requests.packages.urllib3.disable_warnings()

BASE_URL='https://www.hermes.com'

LOG_PURCHASE = "/home/pi/log/purchase.log"

urls = {
  'German': 'https://www.hermes.com/de/de/category/damen/taschen-und-kleinlederwaren/taschen-und-kleine-taschen/',
  # 'IE': 'https://www.hermes.com/ie/en/category/women/bags-and-small-leather-goods/bags-and-clutches'
}

bag_names=[
  'TASCHE LINDY 26'
]


db_connection = {
    'db_host': '192.168.178.20',
    'db_port': '27017',
    'db_name': 'hermes_db',
    'username': 'yl_root',
    'password': 'Cc00114110!',
}

proxy_list = ['berlin', 'ch', 'fr', 'frankfurt2', 'ie', 'se', 'barcelona', 'madrid']

email_config = {
  'sever': '192.168.178.20',
  'port': '465',
  'username': 'toponsky@irishdata.ie',
  'password': 'c00114110!',
  'to': [
    "yimingliu0216@gmail.com"
  ]
}

purchase_server = "http://192.168.178.49:5001"
