"""

    Code source crawler.
    Fait par Florian SILVA et Gabriel BOUT
    
    Version : 1.0

"""

import requests, sys, time 
from requests.exceptions import ConnectionError
from  _Tri import *
from _Req import *



import requests
import time

class Crawler:
    def __init__(self, backup=None):
        
        self.urls_attente = []
        self.urls_down = []
        self.urls_check = {}
        
        if backup is not None :
            backup_file = open(backup,"a")
        
        
        
    def crawl(self, url:str="Wikipedia.org") -> None:
        """
        
        Méthode d'initialisation du crawler.
        
        
        Args :
            url (str) : Le premier url à analiser
            
        Return :
            None.
            
        """
        assert isinstance (url, str), "L'url doit être un str"
        
        
        # Premier url en attente
        self.urls_attente.append(url)
        
        while not len(self.urls_attente) :
            
            start_time = time.time() 
            
            try :
                req = requests.get(url)
                content = req.content
                
                traitement = Trieur(content=content)
                
                
                url = self.urls_attente[1:][0]
                
                end_time = time.time() 
                execution_time = end_time - start_time 
                print(f"Temps d'exécution de la requête pour {url}: {execution_time} secondes")
                    
            except ConnectionError as e :
                print (f"Erreur de connexion sur {url}")
                self.urls_down.append(url)
                url = self.urls_attente[1:][0]
        

    def crawl_from_list(self, list):
        





# Exemple d'utilisation
crawler = Crawler()
first_url = "https://www.figma.com/fr/"
crawler.crawl(first_url)




