"""

    Code source crawler.
    Fait par Florian SILVA et Gabriel BOUT
    
    Version : 1.0

"""
import requests, time, datetime, json, logging, sys, os 
from requests.exceptions import ConnectionError

from Modules._Tri import Trieur
from Modules._Requests import *


import warnings

# Ignorer l'avertissement spécifique concernant les URL dans Beautiful Soup
warnings.simplefilter("ignore")

class Crawler:
    def __init__(self,
                 url_max:int = 10):
        
        assert isinstance (url_max,int)
        
        self.urls_attente = []
        self.urls_down = []
        self.urls_check = {}
        
        self.compteur = 0
        self.url_max = url_max
    
    def crawl(self, url:str, backup:str) -> None:
        """
        Permet de lancer un crawler qui va parcourir tous les liens que l'on croise
        Il récupère tout les informations utiles et les mets dans un dictionnaire
        afin qu'un programme de liaison avec la base de donnée ajoute ces inforamtions
        dans notre base de donnée.
        

        Args:
            url (str): L'url avec lequel on commence le crawler
            backup (str): Le fichier qui permet d'écrire tout les liens en attente
                          pour reprendre là où l'on s'est arrété si le crawler s'arrête
        """
        assert isinstance (url, str), "L'url doit être une chaîne de caractères"
        assert isinstance(backup, str)
        
        url_backup = open(backup,"w")
        self.urls_attente.append(url)
        
        while len(self.urls_attente) > 0 and self.compteur < self.url_max:
            
            start_time = time.time()
             
            try:
                url = self.urls_attente.pop(0)
                
                # Vérifie si l'URL a déjà été visitée
                if url in self.urls_check:
                    continue  # Passe à l'URL suivante si celle-ci a déjà été visitée
                
                print(f"Traitement de : {url}")
                
                content = requests.get(url).content
                tr = Trieur(content, url)
                tr.tri()
                
                info = tr.get_info()
                links = tr.get_links()

                
                for link in links:
                    if link.startswith('#') or link == url:  # Ignore les liens '#' ou les auto-références
                        continue
                    self.urls_attente.append(link)
                
                # Enregistre les informations de l'URL visitée
                self.urls_check[url] = info
                url_backup.write("\n"+url)
                end_time = time.time()
                execution_time = end_time - start_time 

            except ConnectionError as e:
                print(f"Erreur de connexion sur {url}")
                self.urls_down.append(url)
                if len(self.urls_attente) > 0:
                    url = self.urls_attente[0]
            
            self.compteur+=1
        url_backup.close()
                
        

    def crawl_from_list(self, list):
        pass

class CrawlerError (Exception) :
    """
    Something worng with the crawler.
    """
    pass


if __name__ == "__main__" :
    """
    # Clock :
    date = datetime.date.today()
    hour = datetime.datetime.now().replace(microsecond=0).time()
    
    # Initialisation du Logger :
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename=f'*./El-Goog/Server/Logs/{datetime.date.today()}.log', level=logging.INFO)
    
    logger.info(f'----------[Logs du {date}, {hour}]----------')
    """
    # Initialisation du Crawler.
    crawler = Crawler()
    first_url = "https://wikipedia.fr"
    crawler.crawl(first_url, './app/Server/Backup/backup.txt')
    
    """
    # Fin du log.
    logger.info('Finished')

    """

