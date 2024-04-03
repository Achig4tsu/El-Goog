from html.parser import HTMLParser

class Count(HTMLParser):
    def __init__(self):
        super().__init__()
        self.char_count = 0
        
    def count_char(self, html_content):
        self.feed(html_content)
        return self.char_count
    
    def handle_data(self, data):
        self.char_count += len(data.strip())
    
    def handle_comment(self, data):
        # Ignorer les commentaires HTML
        pass
    
    def handle_entityref(self, name):
        # Gérer les références d'entités HTML (par exemple &amp;)
        self.char_count += 1
    
    def handle_charref(self, name):
        # Gérer les références de caractères HTML (par exemple &#32;)
        self.char_count += 1



