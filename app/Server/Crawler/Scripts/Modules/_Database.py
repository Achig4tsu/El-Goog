import mysql.connector
import json
import os
from datetime import datetime, timedelta

class DataBase:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS `Group` (
            Id_groupe INT AUTO_INCREMENT PRIMARY KEY,
            NomGroup VARCHAR(255) UNIQUE,
            Membres VARCHAR(255),
            Rank INT
        )
        """)
        # Création de la table URL
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS URL (
            IDURL INT AUTO_INCREMENT PRIMARY KEY,
            URL VARCHAR(255) UNIQUE,
            Title VARCHAR(255),
            Keywords VARCHAR(255),
            Rank INT,
            IDGroup INT,
            LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (IDGroup) REFERENCES `Group`(IDGroup)
        )
        """)
        # Création de la table URLInfo
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS URLInfo (
            IDURL INT AUTO_INCREMENT PRIMARY KEY,
            URL VARCHAR(255) UNIQUE,
            Title VARCHAR(255),
            Description TEXT
        )
        """)
        # Création de la table Mots_A
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Mots_A (
            IDMots INT AUTO_INCREMENT PRIMARY KEY,
            Mot VARCHAR(255),
            Rank INT
        )
        """)
        # Création de la table Mots_B
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Mots_B (
            IDMots INT AUTO_INCREMENT PRIMARY KEY,
            Mot VARCHAR(255),
            Rank INT
        )
        """)
        # Création de la table Mots_C
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Mots_C (
            IDMots INT AUTO_INCREMENT PRIMARY KEY,
            Mot VARCHAR(255),
            Rank INT
        )
        """)
        self.connection.commit()

    def insert_url(self, url, title, keywords, description, id_group):
        self.cursor.execute("""
        INSERT INTO URL (URL, Title, Keywords, IDGroup)
        VALUES (%s, %s, %s, %s)
        """, (url, title, keywords, id_group))

    def url_exists(self, url):
        self.cursor.execute("""
        SELECT COUNT(*) FROM URL WHERE URL = %s
        """, (url,))
        return self.cursor.fetchone()[0] > 0

    def update_url(self, url, title, keywords, description, id_group):
        self.cursor.execute("""
        UPDATE URL
        SET Title = %s, Keywords = %s, IDGroup = %s
        WHERE URL = %s
        """, (title, keywords, id_group, url))

    def create_group_json(self, id_group, members):
        filename = f"app/Server/Database/Json/GroupeMember_{id_group}.json"
        with open(filename, "w") as f:
            json.dump(members, f)

    def process_url(self, url, title, keywords, description, id_group):
        if not self.group_exists(id_group):
            self.insert_group(id_group)  # Insérer le groupe s'il n'existe pas déjà

        if self.url_exists(url):
            self.update_url(url, title, keywords, description, id_group)
        else:
            self.insert_url(url, title, keywords, description, id_group)

    def group_exists(self, id_group):
        self.cursor.execute("""
        SELECT COUNT(*) FROM `Group` WHERE IDGroup = %s
        """, (id_group,))
        return self.cursor.fetchone()[0] > 0

    def insert_group(self, id_group):
        self.cursor.execute("""
        INSERT INTO `Group` (IDGroup) VALUES (%s)
        """, (id_group,))

    def check_last_update(self, url):
        self.cursor.execute("""
        SELECT LastUpdated FROM URL WHERE URL = %s
        """, (url,))
        last_updated = self.cursor.fetchone()
        if last_updated:
            last_updated = last_updated[0]
            return datetime.now() - last_updated > timedelta(hours=24)
        else:
            return False

    def close(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

def main():
    db = DataBase(host="localhost", user="root", password="", database="El-Goog")

    # Exemple d'insertion d'un URL (à remplacer par les données réelles du crawler)
    url = "http://exemple.com"
    title = "Exemple"
    keywords = "exemple, test, python"
    description = "Ceci est un exemple de description."
    id_group = 1

    # Vérification si l'URL doit être inséré ou mis à jour

    db.process_url(url, title, keywords, description, id_group)

    # Exemple de création du fichier JSON pour la liste des membres de groupe
    members = ["membre1", "membre2", "membre3"]
    db.create_group_json(id_group, members)

    # Fermeture de la connexion à la base de données
    db.close()

if __name__ == "__main__":
    main()
