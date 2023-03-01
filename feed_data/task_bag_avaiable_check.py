import config
from DBManagement import Database as Database
from BagManagement import BagAvailableCheck as Check

if __name__ == "__main__":
    
    db = Database.Database(config.db_connection)
    check = Check.BagAvailableCheck(db)
    check.checkAvailable()
