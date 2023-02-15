from pymongo import MongoClient
from datetime import datetime

class Database:

  def __init__(self, db_config):
    MONGO_HOST = db_config['db_host'] 
    MONGO_PORT = db_config['db_port']
    MONGO_DB = db_config['db_name']
    MONGO_USER = db_config['username']
    MONGO_PASS = db_config['password']

    print("Start connect database: {0}:{1}/{2}".format(MONGO_HOST, MONGO_HOST, MONGO_DB))
    uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_DB)
    client = MongoClient(uri)
    self.database = client[MONGO_DB]
    self.bag_info = self.database.bag_info
    print("Database connected successfully")
    
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
      'is_destroy': False,
      'color_section': 0,
      'is_blocked': False
    }
    self.bag_info.insert_one(bagInfo)

  def findOneBag(self, p_id):
    return self.bag_info.find_one({'id': p_id})  

  def isBagExists(self, p_id):
    if self.bag_info.count_documents({'id': p_id}) > 0:
      return True 
    else:
      return False

  def getBags(self):
    return self.bag_info.find()

  def updateBagStatus(self, _id, isAvailable = True, isDestroy = False, colorSection = 0, isBlocked = False):
    if isBlocked:
      data = {
        'is_blocked': True
      }
    else: 
      data = {
        'is_available': isAvailable,
        'is_destroy': isDestroy,
        'color_section': colorSection,
        'is_blocked': False
      }
    self.bag_info.update_one({'_id':_id}, {"$set": data}, upsert=False)

