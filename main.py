import config
from DBManagement import Database as Database
from BagManagement import BagInfo


if __name__ == "__main__":

    db_config = config.db_connection             
    db = Database.Database(db_config["username"], db_config["password"], db_config["db_name"])
    bag_info = BagInfo.BagInfo(db, config.urls)
    bag_info.collectBagsInfo()
      