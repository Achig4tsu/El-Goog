from rake_nltk import Rake
from nltk.corpus import stopwords

class KeyWord:
    def __init__(self, h1, p, count, mot_useless ) -> None:
        self.h1 = h1 
        self.p = p 
        self.count = count 
        self.mot_useless = mot_useless
        self.val_h1 = 5
        self.val_p = 1 
        
    def extract_keywords(self, text):
        rake = Rake(stopwords=stopwords.words('french'), max_length = 6)
        rake.extract_keywords_from_text(text)
        return rake.get_word_degrees().keys()
    
    def h1_keywords(self):
        return list(set(self.extract_keywords(self.h1)))
    
    def __p_keywords(self):
        return list(set(self.extract_keywords(self.p)))
    
    def calcul_words(self):
        fin = {}
        h1 = self.__h1_keywords()
        p = self.__p_keywords()
        liste_e = set(self.__h1_keywords().append(self.__p_keywords()))
        for i in liste_e :
            
            if i in h1 :
                fin [i] = 5*()
            
        
        
"""
# Exemple d'utilisation
h1 = "Coucou Coucou"
p = "Le contenu de votre page avec plusieurs phrases."
count = 10  # Nombre de mots clés à extraire
mot_useless = []  # Liste de mots à exclure

keyword_extractor = KeyWord(h1, p, count, mot_useless)
print (f"resultat = {keyword_extractor.h1_keywords()}")
"""