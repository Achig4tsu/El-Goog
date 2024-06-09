import time
import datetime
import logging
import os
import json
from Modules._Tri import Trieur
from Modules._Requests import Req
from Modules._Database import MySQLDatabase

class Crawler:
    def __init__(self, config_file='./config.json'):
        self.load_config(config_file)
        self.urls_attente = []
        self.urls_down = []
        self.urls_check = {}
        self.compteur = 0
        self.database = MySQLDatabase(
            host=self.config['database']['host'],
            user=self.config['database']['user'],
            password=self.config['database']['password'],
            database=self.config['database']['database']
        )
        self.setup_logging()

    def load_config(self, config_file):
        try:
            with open(config_file, 'r') as file:
                self.config = json.load(file)
            self.url_max = self.config.get('url_max', 100)
            self.backup_file = self.config.get('backup_file', '/app/Backup/backup.txt')
            self.timeout = self.config.get('timeout', 5)
        except FileNotFoundError:
            logger.error(f'Configuration file "{config_file}" not found.')
            raise
        except json.JSONDecodeError:
            logger.error(f'Error parsing JSON in configuration file "{config_file}".')
            raise

    def setup_logging(self):
        log_file = f'/app/Logs/Crawler/{datetime.datetime.now().date()}.log'
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        logging.basicConfig(filename=log_file, level=logging.INFO)

    def crawl(self, url):
        logger.info(f'Starting crawl for: {url}')
        with open(self.backup_file, "a") as url_backup:
            if os.stat(self.backup_file).st_size == 0:
                url_backup.write(url)
            else:
                url_backup.write("\n" + url)
        self.urls_attente.append(url)
        while len(self.urls_attente) > 0 and self.compteur < self.url_max:
            current_url = self.urls_attente.pop(0)
            logger.info(f'Processing URL: {current_url}')
            url_info = self.database.get_url_info(current_url)
            if url_info:
                title, description, banned, timestamp = url_info
                if not self.database.url_needs_update(timestamp):
                    self.urls_check[current_url] = {'title': title, 'description': description}
                    self._remove_url_from_backup(current_url)
                    continue
            session = Req(current_url)
            content = session.connection()
            if not content:
                self.urls_down.append(current_url)
                self._save_to_down_file(current_url)
                logger.warning(f'Failed to retrieve content from: {current_url}')
                continue
            tr = Trieur(content, current_url)
            tr.tri()
            info = tr.get_info()
            links = tr.get_links()
            for link in links:
                if link.startswith('#') or link == current_url:
                    continue
                if link not in self.urls_attente and link not in self.urls_check:
                    self.urls_attente.append(link)
                    with open(self.backup_file, "a") as url_backup:
                        url_backup.write("\n" + link)
            if not info.get('banned'):
                self.database.insert_url_info(current_url, info['title'], info['description'])
                self.database.create_group_if_not_exists(info['group'])
                self.database.add_url_to_group(current_url, info['group'])
                for keyword in info.get('keywords', []):
                    self.database.add_keyword_to_table(keyword)
            self.urls_check[current_url] = info
            self._remove_url_from_backup(current_url)
            end_time = time.time()
            execution_time = end_time - start_time
            self.compteur += 1
            logger.info(f'Crawled {current_url} in {execution_time:.2f}s, {self.compteur}/{self.url_max} completed.')

        logger.info('Finished crawling all URLs.')

    def _remove_url_from_backup(self, url):
        with open(self.backup_file, "r") as file:
            lines = file.readlines()
        with open(self.backup_file, "w") as file:
            for line in lines:
                if line.strip() != url:
                    file.write(line)

    def _save_to_down_file(self, url):
        down_file_path = os.path.join(os.path.dirname(self.backup_file), 'down.txt')
        with open(down_file_path, "a") as down_file:
            down_file.write(url + "\n")

if __name__ == "__main__":
    logger = logging.getLogger("Crawler")
    crawler = Crawler(config_file="./config.json")
    first_url = "https://google.com"
    crawler.crawl(first_url)
    logger.info('Finished crawling process.')
