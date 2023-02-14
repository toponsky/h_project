import config
from DBManagement import Database as Database
from BagManagement import BagInfo, BagStatus
from ProxyManagement import ProxyManager
import time

if __name__ == "__main__":

    db_config = config.db_connection             
    db = Database.Database(db_config["username"], db_config["password"], db_config["db_name"])
    # bag_info = BagInfo.BagInfo(db, config.urls)
    # bag_info.collectBagsInfo()

    # bag_status = BagStatus.BagStatus(db)
    # bag_status.checkAvailable()


    proxyMger = ProxyManager.ProxyManager(config.proxy_list)
    
   
    proxyMger.startNextProxy()
    time.sleep(3)
    proxyMger.startNextProxy()
    time.sleep(3)
    proxyMger.startNextProxy()
    time.sleep(3)
    proxyMger.stop()
