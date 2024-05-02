from Modules._Keywords import KeyWord
from Modules._Finder import Find
from Modules._Cleaner import Cleaner

"""
Module permettant de centraliser le tri des information d'une page
Ce module donne les informations finales que l'on utilisera dans la 
base de donnée.

** Fonctionnement : ** 

    1 - Finder : On cherche toutes les balises qui nous intéresse (h1,p,etc...)
    2 - Cleaner : On nettoie ces balises car il arrive que certains site
                  mette des balises complémentaire au sein d'une balise qui nous intéresse.
    3 - Keywords : Il prend chaque balise une par une et en ressort les mots clé uniquement.
    4 - Le tri : C'est ici que tout se passe on accorde tout nos instruments pour assurer 
                 un fonctionnement optimal lors de l'entrainement de nos bases de données.

Return  :
    méthode principale (tri) : 
    dict : {
    
        title : (str)
        description : (str)
        links : (list)
        keywords : (list)
        banned : (bool)

    }
"""


class Trieur :
    
    
    def __init__(self, content, url) -> None:
        
        self.url = url

        # Return 
        self.__title = ""
        self.__description = ""
        self.__links = []
        self.__keywords = []
        self.__banned = False
        
        
        # Content page :
        self.__content = content
    

        """
        Attention à bien penser à trié le dict en fonction du degré le plus fort !
        """
        return 





    def tri(self) :

        find = Find(self.__content)

        # -- Recuperation des éléments de la page

        unclean_title = find.find_all()["title"]
        unclean_description = find.find_all()["description"]
        unclean_links = find.find_all()["links"]
        unclean_h1 = find.find_all()["h1"]
        unclean_p = find.find_all()["p"]

        # -- Nettoyage des éléments de la page 

        
        clean_title = Cleaner(self.url, unclean_title).clean()
        clean_description = Cleaner(self.url, unclean_description).clean()
        clean_h1 = Cleaner(self.url, unclean_h1).clean()
        clean_links = Cleaner(self.url, unclean_links).clean()
        clean_p = Cleaner(self.url, unclean_p).clean()

    
    
        k = KeyWord(
            title = clean_title,
            description = clean_description,
            h1 = clean_h1,
            p = clean_p
        )
        
        self.__title = clean_title
        self.__description = clean_description
        self.__links = clean_links
        self.__banned = False # Changera dans une mise a jour futur.
        self.__keywords = k.get_raw_keywords()
        print (self.__keywords)

        return

    def get_info(self):
        return {
            "title" : self.__title,
            "description" : self.__description,
            "keywords" : self.__keywords,
            "banned" : False
        }
                
    def get_links(self):
        return self.__links
        

if __name__ =="__main__": 
    pass