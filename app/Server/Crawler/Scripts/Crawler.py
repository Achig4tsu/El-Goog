import time
import datetime
import json
import logging
import os 
from Modules._Tri import Trieur
from Modules._Requests import Req

import warnings
warnings.simplefilter("ignore")

logger = logging.getLogger("Crawler.py")


class Preferences:
    def __init__(self, url_max: int = 100, backup_file: str = 'app/Server/Crawler/Backup/backup.txt', preferences_file: str = './preferences.json', timeout: int = 5):
        self.url_max = url_max
        self.backup_file = backup_file
        self.preferences_file = preferences_file
        self.timeout = timeout
        
    def load_from_file(self, file_path: str) -> None:
        try:
            with open(file_path, 'r') as file:
                preferences = json.load(file)
                self.url_max = preferences.get('url_max', self.url_max)
                self.backup_file = preferences.get('backup_file', self.backup_file)
                self.preferences_file = preferences.get('preferences_file', self.preferences_file)
                self.timeout = preferences.get('timeout', self.timeout)
        except FileNotFoundError:
            logger.warning(f'Preferences file "{file_path}" not found. Using default preferences.')
        except json.JSONDecodeError:
            logger.warning(f'Error parsing JSON in preferences file "{file_path}". Using default preferences.')
    
    def save_to_file(self, file_path: str) -> None:
        preferences = {
            'url_max': self.url_max,
            'backup_file': self.backup_file,
            'preferences_file': self.preferences_file,
            'timeout': self.timeout
        }
        with open(file_path, 'w') as file:
            json.dump(preferences, file, indent=4)

class Crawler:
    def __init__(self, url_max: int = 100, preferences_file: str = './preferences.json'):
        self.urls_attente = []  # Initialisez la liste des URLs à parcourir
        self.urls_down = []
        self.urls_check = {}
        self.compteur = 0
        self.preferences = Preferences(url_max=url_max)
        self.preferences.load_from_file(preferences_file)
        self.timeout = self.preferences.timeout  # Initialisez également le timeout
        
    def save_preferences(self):
        self.preferences.save_to_file(self.preferences.preferences_file)
    
    def set_preferences(self, preferences: dict) -> None:
        """
        Met à jour les préférences du crawler en fonction des paramètres fournis.

        Args:
            preferences (dict): Dictionnaire contenant les nouvelles préférences du crawler.
        """
        self.preferences.url_max = preferences.get('url_max', self.preferences.url_max)
        self.preferences.backup_file = preferences.get('backup_file', self.preferences.backup_file)
        self.preferences.preferences_file = preferences.get('preferences_file', self.preferences.preferences_file)
        self.preferences.timeout = preferences.get('timeout', self.preferences.timeout)
        
        self.save_preferences()
        
    def crawl(self, url: str) -> None:
        assert isinstance(url, str), "L'URL doit être une chaîne de caractères"
        
        # Ouvrir le fichier de sauvegarde
        with open(self.preferences.backup_file, "a") as url_backup:
            # Écrire l'URL dans le fichier de sauvegarde
            if os.stat(self.preferences.backup_file).st_size == 0:
                url_backup.write(url)
            else:
                url_backup.write("\n" + url)
        
        while len(self.urls_attente) > 0 and self.compteur < self.preferences.url_max:
            start_time = time.time()
            url = self.urls_attente.pop(0)

            # Vérifie si l'URL a déjà été visitée
            if url in self.urls_check:
                # Si l'URL a été visitée, la supprimer du fichier de sauvegarde
                with open(self.preferences.backup_file, "r+") as f:
                    lines = f.readlines()
                    f.seek(0)
                    for line in lines:
                        if line.strip() != url:
                            f.write(line)
                    f.truncate()
                continue

            session = Req(url, timeout=self.timeout)
            
            if session.is_site_down():
                self.urls_down.append(url)
                continue
            content = session.connection()
            tr = Trieur(content, url)
            tr.tri()
            info = tr.get_info()
            links = tr.get_links()
            
            for link in links:
                if link.startswith('#') or link == url:
                    continue
                self.urls_attente.append(link)
                
                # Ajoute le nouveau lien au fichier de sauvegarde
                with open(self.preferences.backup_file, "a") as url_backup:
                    url_backup.write("\n" + link)
            
            # Enregistre les informations de l'URL visitée
            self.urls_check[url] = info
            end_time = time.time()
            execution_time = end_time - start_time
            self.compteur += 1
    
    def crawl_from_list(self) -> None:
        """
        Reprend la session de crawling à partir d'une liste de liens stockée dans un fichier de sauvegarde.
        """
        with open(self.preferences.backup_file, "r") as url_backup:
            urls = url_backup.readlines()
        
        for url in urls:
            url = url.strip()  # Retire les espaces et les sauts de ligne
            self.urls_attente.append(url)  # Ajoutez l'URL à la liste des URLs à parcourir
            self.crawl(url)  # Appel à la méthode crawl pour parcourir l'URL


if __name__ == "__main__":
    date = datetime.date.today()
    hour = datetime.datetime.now().replace(microsecond=0).time()
        
    logging.basicConfig(filename=f'./app/Server/Crawler/Logs/Crawler/{datetime.date.today()}.log', level=logging.INFO)
    logger.info(f'----------[Logs du {date}, {hour}]----------')
    
    # Initialisation du Crawler
    crawler = Crawler(preferences_file="app/Server/Crawler/Scripts/preferences.json")
    
    # Test de la méthode crawl
    first_url = "https://wikipedia.fr"
    crawler.crawl(first_url)
    
    # Test de la méthode crawl_from_list


    logger.info('Finished')
