import requests
from bs4 import BeautifulSoup

'''
    Vous chercher toutes les infos utiles de la page ? Vous vous trouvez au bon endroit ! Ici vos problemes sont résolus et vous pourrez retrouver sous forme de liste ou Tuple
    le Titre (Si tout fonctionne -> string et pas liste), les balises <h1>, <p> (Sous forme de listes), la description de la page et tout les liens href (Sous forme de Liste) !!!
    A Tester avant utilisation ces commandes peuvent étres fausses.
'''

class Find :
    def __init__(self,content) -> None:
        self.content = content
        self.soup = BeautifulSoup(self.content, features='html.parser')
    
    
    def FindTitle(self):
        '''
        Recherche les balises <title> dans le contenu HTML.

        Retourne :
            list: Une liste contenant la balise Title trouver dans le code HTML de la page
        '''
        return self.soup.title.string # Si marche pas remettre self.soup.find('title')
    
    def FindH1(self):
        '''
        Recherche les balises <h1> dans le contenu HTML.

        Retourne :
            list: Une liste contenant les balise h1 trouver dans le code HTML de la page ou False si il y a plus d'une balise h1
        '''
        h1 = self.soup.find_all('h1')
        if len(h1) > 1:
            return False
        return h1
    
    def FindP(self):
        '''
        Recherche les balises <p> dans le contenu HTML.

        Retourne :
            list: Une liste contenant les balise p trouver dans le code HTML de la page
        '''
        return self.soup.find_all('p')
    
    
    def FindDes(self):
        return self.soup.find('meta', attrs={'name' : 'description'})['content']
    
    def Findhref(self):
        '''
        Recherche tout les href d'une page HTML

        Retourne :
            list : Une liste qui contient tout les href (liens) de la page HTML
        '''
        return [a['href'] for a in self.soup.find_all('a', href=True)]

    def find_all (self):
        '''
        Assemble toutes les données en un tableau

        Retourne :
            Tuple : Un tuple contenant les Titres, balises <h1>, <p> et la description de la page HTML

        '''
        return [self.FindTitle() , self.FindH1() , self.FindP() , self.FindDes()]
    
req = requests.get('https://rassemblementnational.fr/', allow_redirects=True)
content = req.content
a = Find(content)