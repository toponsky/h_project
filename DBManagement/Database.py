from pymongo import MongoClient
from datetime import datetime

class Database:

  def __init__(self, db_username, db_password, db_name):
    MONGO_HOST = "192.168.178.20" 
    MONGO_PORT = "27017"
    MONGO_DB = db_name
    MONGO_USER = db_username
    MONGO_PASS = db_password
    uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_DB)
    client = MongoClient(uri)
    self.database = client[MONGO_DB]
    self.bag_info = self.database.bag_info
    
  def insertOneBag(self, p_id, p_url, p_img_url, p_name, p_color, p_price):
    bagInfo = { 
      "id": p_id,
      "url": p_url, 
      "img_url": p_img_url,
      "name": p_name,
      "color": p_color,
      "p_price": p_price,
      "create_time": datetime.now(),
      'is_available': True,
      'is_destroy': False
    }
    self.bag_info.insert_one(bagInfo)

  def isBagExists(self, p_id):
    if self.bag_info.count_documents({'id': p_id}) > 0:
      return True 
    else:
      return False

  def getBags(self):
    return self.bag_info.find()

