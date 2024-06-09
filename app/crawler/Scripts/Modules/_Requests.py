import requests
from requests.exceptions import ConnectionError, Timeout, RequestException
import random

class Req:
    def __init__(self, url: str, timeout: int = 5000) -> None:
        assert isinstance(url, str), "URL must be a string"
        self.url = url
        self.timeout = timeout
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3', 
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0', 
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15'
        ]
        self.accepts = [
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
        ]
        self.accept_languages = [
            'en-US,en;q=0.9',
            'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7'
        ]
        self.accept_encodings = [
            'gzip, deflate, br',
            'gzip, deflate',
            'br, gzip, deflate'
        ]
        self.connections = [
            'keep-alive',
            'close'
        ]

    def get_random_user_agent(self) -> str:
        return random.choice(self.user_agents)
    
    def get_random_timeout(self) -> int:
        return random.randint(1, self.timeout)
    
    def generate_headers(self) -> dict:
        headers = {
            'User-Agent': self.get_random_user_agent(),
            'Accept': random.choice(self.accepts),
            'Accept-Language': random.choice(self.accept_languages),
            'Accept-Encoding': random.choice(self.accept_encodings),
            'Connection': random.choice(self.connections),
            'Referer': self.url
        }
        return headers
    
    def test_connection(self) -> bool:
        headers = self.generate_headers()
        try:
            response = requests.head(self.url, headers=headers, timeout=self.get_random_timeout(), allow_redirects=True)
            return response.status_code == 200
        except (ConnectionError, Timeout, RequestException):
            return False

    def is_pdf(self) -> bool:
        return self.url.endswith('.pdf')

    def is_site_down(self) -> bool:
        headers = self.generate_headers()
        try:
            response = requests.head(self.url, headers=headers, timeout=self.get_random_timeout(), allow_redirects=True)
            # Un site n'est pas considéré comme down s'il répond avec un code de redirection 3xx
            print(response.status_code)
            return not (200 <= response.status_code < 400)
        except (ConnectionError, Timeout, RequestException):
            return True

    def connection(self) -> str:
        headers = self.generate_headers()
        try:
            response = requests.get(self.url, headers=headers, timeout=self.get_random_timeout(), allow_redirects=True)
            return response.content
        except (ConnectionError, Timeout, RequestException):
            return "Failed to connect or timeout occurred"




