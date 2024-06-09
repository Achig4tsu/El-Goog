import bs4

class Cleaner :
    
    def __init__(self, url, content) -> None:
        assert isinstance(url, str)
        assert isinstance(content, str) or isinstance(content, list)

        self.__url = url 
        self.__content = content

        
    def __clean(self, text) :
        return bs4.BeautifulSoup(text, 'lxml').get_text()
    
    def clean(self):
        
        l = []
        
        if self.__content is None or '' :
            return ''
        
        elif isinstance(self.__content, list) :
            for i in self.__content :
                clean = self.__clean(i)
                if clean == "" or None :
                    continue
                elif clean[0] == '#' :
                    clean = self.__url + "/" + clean[:1]
                elif "@" in clean :
                    continue
                elif clean[0] == "/" :
                    clean = self.__url + clean
                l.append(clean)
            return l 
        
        elif isinstance(self.__content, str) :
            return self.__clean(self.__content)
        
    
        
        else :
            raise ErrorCleaner("Cleaner problem..")
                

class ErrorCleaner(Exception):
    pass

if __name__ == "__main__" :
    pass