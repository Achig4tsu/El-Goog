import re
from rake_nltk import Rake
import nltk
from nltk.corpus import stopwords

# Télécharger les ressources nécessaires si elles ne sont pas déjà téléchargées
nltk.download("punkt")
nltk.download("stopwords")

class KeyWord:
    def __init__(self, **kwargs) -> None:
        self.__var = 8
        self.__elements = kwargs
        self.__num_keywords = 10  # Nombre de mots clés par défaut
        
        # Paramètres :
        
        # Coefficients de pondération :
        self.__coefficients = {
            "h1": 5,
            "title": 10,
            "p": 2,
            "balises": 1
        }
        
        # Coefficients d'occurrence :
        self.__occurrence_coefficients = {
            "p": 0.5,
            "balises": 0.3
        }
        
    def set_num_keywords(self, num_keywords):
        self.__num_keywords = num_keywords
        
    def get_keyword_coefficients(self):
        return self.__coefficients
    
    def __extract_keywords(self, text):
        # Retirer la ponctuation
        text = re.sub(r'[^\w\s]', '', text)
        all_stopwords = []
        for lang in nltk.corpus.stopwords.fileids():
            all_stopwords.extend(nltk.corpus.stopwords.words(lang))

        rake = Rake(stopwords=all_stopwords, max_length=self.__var)
        rake.extract_keywords_from_text(text)
        return rake.get_word_frequency_distribution()
    
    def __count_occurrences(self, text, keywords):
        occurrences = {}
        for word in keywords:
            count = text.lower().count(word)
            occurrences[word] = count
        return occurrences
    
    def __calculate_keyword_value(self, keyword, occurrences):
        value = 0
        for element, text in self.__elements.items():
            coefficient = self.__coefficients.get(element, 1)  # Par défaut, coefficient = 1
            if element in ["h1", "title"]:
                coefficient *= 5  # Coefficient multiplié par 5 pour h1 et title
            elif element == "p":
                coefficient *= 2  # Coefficient multiplié par 2 pour les balises p
                
            # Calcul de la valeur en fonction des occurrences
            if element in ["h1", "title", "p"]:
                occurrence_coefficient = self.__occurrence_coefficients.get("p", 1)
            else:
                occurrence_coefficient = self.__occurrence_coefficients.get("balises", 1)
                
            value += coefficient * occurrences.get(keyword, 0) * occurrence_coefficient
        
        return value
    
    def __setup(self) -> None:
        self.__keywords = {}
        for element, text in self.__elements.items():
            keywords = self.__extract_keywords(text)
            occurrences = self.__count_occurrences(text, keywords.keys())
            keyword_values = {keyword: self.__calculate_keyword_value(keyword, occurrences) for keyword in keywords.keys()}
            self.__keywords[element] = sorted(keyword_values.items(), key=lambda x: x[1], reverse=True)[:self.__num_keywords]
    
    def get_all_keywords(self) -> list:
        """
        Méthode GET qui renvoie les mots clés de chaque élément
        d'une page web et ce séparément.

        Return  :
            (list) : Liste des mots clés

        """
        self.__setup()
        consolidated_keywords = {}
        for element_keywords in self.__keywords.values():
            for keyword, value in element_keywords:
                if keyword not in consolidated_keywords:
                    consolidated_keywords[keyword] = value
                else:
                    consolidated_keywords[keyword] += value
        consolidated_keywords = sorted(consolidated_keywords.items(), key=lambda x: x[1], reverse=True)
        return consolidated_keywords[:self.__num_keywords]
    
    
    def get_raw_keywords(self) -> list:
        """
        Méthode GET qui renvoie les mots clés bruts de chaque élément
        d'une page web, sans les coefficients.

        Return  :
            (list) : Liste des mots clés

        """
        self.__setup()
        raw_keywords = []
        for element_keywords in self.__keywords.values():
            for keyword, _ in element_keywords:
                if keyword not in raw_keywords:
                    raw_keywords.append(keyword)
        return raw_keywords


if __name__ == "__main__":
    pass
