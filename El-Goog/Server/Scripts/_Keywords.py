from rake_nltk import Rake
from nltk.corpus import stopwords

class KeyWord:
    def __init__(self,
                 title : str = "",
                 h1 : str = "",
                 description : str = "",
                 p : str = "",
                 balises : str = ""
                 ) -> None:
        
        self.__title = title
        self.__h1 = h1 
        self.__description = description
        self.__p = p
        self.__balises = balises
        
        self.__var = 6
    
    def __extract_keywords(self, text):
        rake = Rake(stopwords=stopwords.words("french"), max_length=self.__var)
        rake.extract_keywords_from_text(text)
        return rake.get_word_degrees().keys()
    
    def __setup (self) -> None :
        self.__title = list(set(self.__extract_keywords(self.__title)))   
        self.__h1 = list(set(self.__extract_keywords(self.__h1)))
        self.__description= list(set(self.__extract_keywords(self.__description)))
        self.__p = list(set(self.__extract_keywords(self.__p)))
        self.__balises = list(set(self.__extract_keywords(self.__balises)))

    def get_all_keywords(self) -> dict :
        """
        Méthode GET qui renvoi les mots clé de chaques élément 
        d'une page web et ce séparèment.
        
        Return  :
            (dict) : Dictionnaire des mots clés 
        
        """        
        self.__setup()
        return {
            "title" : self.__title,
            "h1" : self.__h1,
            "description" : self.__description,
            "p" : self.__p,
            "balises" : self.__balises            
        }

            
