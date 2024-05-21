"""

Module de requêtes.

Fait par : - SILVA Florian
           - BOUT Gabriel
           
Version : 1.0

"""
import requests
from requests.exceptions import ConnectionError, Timeout

class Req:
    def __init__(self, url: str, timeout: int = 5) -> None:
        assert isinstance(url, str), "URL must be a string"
        self.url = url
        self.timeout = timeout

    def test_connection(self) -> bool:
        try:
            response = requests.head(self.url, timeout=self.timeout)
            return response.status_code == 200
        except (ConnectionError, Timeout):
            return False

    def is_pdf(self) -> bool:
        return self.url.endswith('.pdf')

    def is_site_down(self) -> bool:
        try:
            response = requests.head(self.url, timeout=self.timeout)
            return response.status_code != 200
        except (ConnectionError, Timeout):
            return True

    def generate_html_headers(self) -> dict:
        headers = {
            'Content-Type': 'text/html',
            'charset': 'utf-8'
        }
        return headers

    def connection(self) -> str:
        try:
            response = requests.get(self.url, headers=self.generate_html_headers(), timeout=self.timeout)
            return response.content
        except (ConnectionError, Timeout):
            return "Failed to connect or timeout occurred"

