from pymongo import MongoClient
from datetime import datetime

class Database:

  def __init__(self, db_username, db_password):
    self.username = db_username
    self.password = db_username
    # self.database = pymongo.MongoClient("mongodb://{0}:{0}@192.168.178.20/hermes_db".format(self.username, self.password))['hermes_db']['user']
    MONGO_HOST = "192.168.178.20" 
    MONGO_PORT = "27017"
    MONGO_DB = "hermes_db"
    MONGO_USER = "yl_root"
    MONGO_PASS = "Cc00114110!"
    uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_DB)
    client = MongoClient(uri)
    self.database = client["hermes_db"]
    self.bag_info = self.database.bag_info
    # self.database = client['hermes_db']
    # # result = self.database.user.find()

    # # for document in result:
    # #     print(document)
    
  def insertOneBag(self,p_id, name, imageUrl, url):
    bagInfo = { 
      "p_id": p_id,
      "name": name, 
      "create_time": datetime.now(),
      "image_url": imageUrl,
      "url": url
    }
    self.bag_info.insert_one(bagInfo)


