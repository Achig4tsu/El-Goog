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
    def __init__(self):
        self.File = []
        self.Down = []
        self.Urls = {}
        
    def crawl(self, url):
        start_time = time.time()  # Mesure le temps au début de la requête
        
        try:
            response = requests.get(url)
            content = response.content
            
            # Traitement :
            
            traitement = Trieur(content)
            print(traitement.tri()[1])
            
            
            
            
            end_time = time.time()  # Mesure le temps à la fin de la requête
            execution_time = end_time - start_time  # Calcule le temps d'exécution de la requête
            print(f"Temps d'exécution de la requête pour {url}: {execution_time} secondes")
            
        except ConnectionError as e:
            print(f"Erreur de connexion pour {url}: {e}")

# Exemple d'utilisation
crawler = Crawler()
first_url = "https://www.figma.com/fr/"
crawler.crawl(first_url)




