import mysql.connector, json, os, datetime, logging

logging.basicConfig(filename=f"../../Logs/Database/{datetime.date.today()}.log",level=logging.INFO)

logger = logging.getLogger("DataBase_Constructor")


class DataBase:
    
    def __init__(self,
                 host:str,
                 user:str,
                 password:str,
                 database:str
                 ) -> None:
        
        try :
            self.connection = mysql.connector.connect(
                host = host,
                user = user,
                password = password,
                database = database
            )
            
            self.cursor = self.connection.cursor()
            self.create_tables()
            
        except mysql.connector.Error as Err :
            raise ConnexionError(f"Erreur lors de la connexion à la base de donnée :{Err}")


    def create_tables(self) :
        pass
    
    
    
    
    
    
class ConnexionError(Exception):
    logger.critical("ERREUR DE CONNEXION")
    
    
if __name__ == "__main__" :    
    D = DataBase("localhost", "root", "blabla", "El-Goog")
    