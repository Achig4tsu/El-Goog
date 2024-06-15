import bs4

class Cleaner:
    
    def __init__(self, url, content) -> None:
        assert isinstance(url, str)
        assert isinstance(content, str) or isinstance(content, list)

        self.__url = url 
        self.__content = content

    def __clean(self, text):
        return bs4.BeautifulSoup(text, 'lxml').get_text()
    
    def clean(self):
        l = []
        if self.__content is None or self.__content == '':
            return ''
        elif isinstance(self.__content, list):
            for i in self.__content:
                clean = self.__clean(i)
                if clean == "" or clean is None:
                    continue
                elif clean[0] == '#':
                    clean = self.__url + "/" + clean[:1]
                elif "@" in clean:
                    continue
                elif clean[0] == "/":
                    clean = self.__url + clean
                l.append(clean)
            return l 
        elif isinstance(self.__content, str):
            return self.__clean(self.__content)
        else:
            raise ErrorCleaner("Cleaner problem..")

    def should_ban_site(self):
        soup = bs4.BeautifulSoup(self.__content, 'html.parser')
        # Check for multiple <h1> tags
        h1_tags = soup.find_all('h1')
        if len(h1_tags) > 1:
            return True
        # Check for W3C compliance
        if not self.check_w3c_compliance(self.__content):
            return True
        return False

    def check_w3c_compliance(self, html_content):
        # Placeholder for W3C compliance check
        return True  # Assume compliance for now

class ErrorCleaner(Exception):
    pass

if __name__ == "__main__":
    pass
