from _Keywords import *
from _Finder import *
from _Counter import *



class Trieur :
    
    
    def __init__(self, content) -> None:
        
        # Return 
        self.__title = ""
        self.__description = ""
        self.__links = []
        self.__keywords = []
        
        
        # Content page :
        self.__content = content
        
        # Finder elements :
        finder = Find(content=self.__content)
        
        self.__h1 = finder.FindH1()
        self.__p = finder.FindP()
        
        self.__finder_links = finder.Findhref()
        self.__finder_title = finder.FindTitle()
        self.__finder_Description = finder.FindDes()
        
        # Paramètres :
        
            # Val find :
        self.__val_h1 = 5
        self.__val_title = 3
        self.__val_p = 2
        self.__val_balises = 1
        
            # Val occu :
        self.__val_occu_p = 0.5
        self.__val_occu_balises = 0.3
        
        """
        Attention à bien penser à trié le dict en fonction du degré le plus fort !
        """
        
        
        
        
        
        
        
    def tri (self) -> dict :
        """
        
        Setup de l'algotythme de tri de la page.
        
        Args :
            None
        
        Return :
            (dict) : (mot : valeur)
        
        """
        
        if not self.__h1  :
            return False 
        
        
        dic = {
            
        }
        
        Keyword = KeyWord(self.__title, self.__h1,self.description, self.__p)   
        all_kw = Keyword.get_all_keywords()
        
        title = all_kw["title"]
        h1 = all_kw["h1"]
        description = all_kw["description"]        
        
             
        total_mots = self.__title + self.__h1 + self.__description
        
        for mot in range (total_mots + self.__p) :
            
            if mot in 
