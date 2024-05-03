import mysql.connector
import json
import os
from datetime import datetime, timedelta
import logging


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
            
        except mysql.connector.Error as Err :
            raise ConnexionError(f"||ERREUR|| : Erreur lors de la connexion à la base de donnée :{Err}")


class ConnexionError(Exception):
    