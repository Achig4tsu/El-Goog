from bs4 import BeautifulSoup

class Find:
    def __init__(self, content) -> None:
        self.content = content
        self.soup = BeautifulSoup(self.content, features='html.parser')

    def find_tag(self, tag_name):
        """
        Recherche les balises spécifiées dans le contenu HTML.

        Arguments:
            tag_name (str): Le nom de la balise à rechercher, par exemple 'h1', 'p', 'h2', etc.

        Retourne :
            list: Une liste contenant les balises trouvées dans le code HTML de la page.
        """
        return str(self.soup.find_all(tag_name)) or ""

    def find_title(self):
        """
        Recherche la balise <title> dans le contenu HTML.

        Retourne :
            str: Le contenu texte de la balise Title trouvée dans le code HTML de la page, ou None si elle n'est pas trouvée.
        """
        title_tag = self.soup.title
        if title_tag:
            return str(title_tag.string)
        return ""

    def find_description(self):
        """
        Recherche la balise <meta name='description'> dans le contenu HTML.

        Retourne :
            str: Le contenu de l'attribut 'content' de la balise meta avec 'name' égal à 'description', ou None si elle n'est pas trouvée.
        """
        description_tag = self.soup.find('meta', attrs={'name': 'description'})
        if description_tag:
            return str(description_tag.get('content'))
        return ""

    def find_href(self):
        """
        Recherche tous les href (liens) dans les balises <a> du contenu HTML.

        Retourne :
            list : Une liste qui contient tous les href (liens) trouvés dans les balises <a> du code HTML de la page.
        """
        return [a['href'] for a in self.soup.find_all('a', href=True)] or ""

    def find_all(self):
        """
        Assemble toutes les données en un dictionnaire.

        Retourne :
            Dictionnaire contenant les éléments trouvés dans le code HTML de la page.
        """
        return {
            "title": self.find_title(),
            "description": self.find_description(),
            "links": self.find_href(),
            "h1": self.find_tag('h1'),
            "h2": self.find_tag('h2'),
            "h3": self.find_tag('h3'),
            "p": self.find_tag('p')
        }

# Test de la classe Find
if __name__ == "__main__":
    content = """
    <html>
    <head>
    <title>Test Title</title>
    <meta name="description" content="Test Description">
    </head>
    <body>
    <h1>Heading 1</h1>
    <h2>Heading 2</h2>
    <h3>Heading 3</h3>
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
    <a href="https://example.com">Link 1</a>
    <a href="https://example.org">Link 2</a>
    </body>
    </html>
    """
    f = Find(content)
    print(f.find_all())
