import config
from DBManagement import Database as Database
from BagManagement import BagInfo, BagStatus
from ProxyManagement import ProxyManager
from EmailManagement import EmailManager
import time

if __name__ == "__main__":
    
    db = Database.Database(config.db_connection)
    proxies = ProxyManager.ProxyManager(config.proxy_list)
    email = EmailManager.EmailManager(config.email_config)
    # # bag_info = BagInfo.BagInfo(db, config.urls)
    # # bag_info.collectBagsInfo()
   
    bag_status = BagStatus.BagStatus(db, proxies, email)
    bag_status.checkAvailable()
