-- Création de la table urls pour stocker les URLs
CREATE TABLE urls (
    id_url INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    titre VARCHAR(255),
    description TEXT,
    mot_cle VARCHAR(255)
);

-- Création de l'index sur la colonne url de la table urls
CREATE INDEX idx_url ON urls (url);

-- Création de la table Url_MotCle pour gérer la relation many-to-many entre les URLs et les mots-clés
CREATE TABLE Url_MotCle (
    id_url INT,
    mot_cle VARCHAR(255),
    FOREIGN KEY (id_url) REFERENCES urls(id_url) ON DELETE CASCADE,
    PRIMARY KEY (id_url, mot_cle)
);

-- Création des tables pour les mots par lettre de l'alphabet
-- Note : Vous pouvez répéter ce bloc de création pour chaque lettre de l'alphabet
CREATE TABLE Mot_a (
    mot_id INT AUTO_INCREMENT PRIMARY KEY,
    mot VARCHAR(255),
    id_url INT,
    priority_val INT,
    counter INT,
    final INT,
    FOREIGN KEY (id_url) REFERENCES urls(id_url) ON DELETE CASCADE
);

-- Création de l'index sur la colonne mot de chaque table de mots
CREATE INDEX idx_mot_a_mot ON Mot_a (mot);
-- Vous pouvez répéter cette instruction pour chaque table de mots (Mot_b, Mot_c, etc.)

-- Création de la table url_info pour stocker les informations essentielles pour l'affichage web
CREATE TABLE url_info (
    url_id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255),
    title VARCHAR(255),
    description TEXT
);

-- Création de l'index sur la colonne url de la table url_info
CREATE INDEX idx_url_info_url ON url_info (url);


-- Insertion des données dans la table urls
INSERT INTO urls (url, titre, description, mot_cle) VALUES
('http://exemple.com/page1', 'Page 1', 'Description de la page 1', 'exemple, page'),
('http://exemple.com/page2', 'Page 2', 'Description de la page 2', 'exemple, page'),
('http://exemple.com/page3', 'Page 3', 'Description de la page 3', 'exemple, page');

-- Insertion des données dans la table Url_MotCle
INSERT INTO Url_MotCle (id_url, mot_cle) VALUES
(1, 'exemples'),
(1, 'mots-clés'),
(2, 'exemples'),
(2, 'mots-clés');

-- Insertion des données dans la table Mot_a
INSERT INTO Mot_a (mot, id_url, priority_val, counter, final) VALUES
('exemple', 1, 5, 10, 50),
('mots-clés', 1, 3, 8, 24),
('autre', 2, 7, 15, 105);

-- Insertion des données dans la table url_info
INSERT INTO url_info (url, title, description) VALUES
('http://exemple.com/page1', 'Titre de la page 1', 'Description de la page 1'),
('http://exemple.com/page2', 'Titre de la page 2', 'Description de la page 2'),
('http://exemple.com/page3', 'Titre de la page 3', 'Description de la page 3');
