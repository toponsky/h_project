import config
from DBManagement import Database as Database
from BagManagement import BagInfo, BagStatus
from EmailManagement import EmailManager

if __name__ == "__main__":
    
    db = Database.Database(config.db_connection)
    email = EmailManager.EmailManager(config.email_config)
   
    bag_status = BagStatus.BagStatus(db, email)
    bag_status.checkAvailable()

