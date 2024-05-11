-- Création de la base de données
CREATE DATABASE IF NOT EXISTS El_Goog
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- Sélection de la base de données
USE El_Goog;

-- Création de la table pour les groupes
CREATE TABLE IF NOT EXISTS `Group` (
    IDGroup INT AUTO_INCREMENT PRIMARY KEY,
    NomGroup VARCHAR(255) UNIQUE,
    Membres VARCHAR(255),
    Rank INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Création de l'index sur la colonne NomGroup
CREATE INDEX idx_NomGroup ON `Group` (NomGroup);

-- Création de la table pour les URL
CREATE TABLE IF NOT EXISTS 'Urls' (
    IDURL INT AUTO_INCREMENT PRIMARY KEY,
    URL VARCHAR(255) UNIQUE,
    Title VARCHAR(255),
    Keywords VARCHAR(255),
    Rank INT,
    IDGroup INT,
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (IDGroup) REFERENCES `Group`(IDGroup)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Création de l'index sur la colonne URL
CREATE INDEX idx_URL ON 'Urls' (URL);

-- Création de la table pour les informations d'URL
CREATE TABLE IF NOT EXISTS URLInfo (
    IDURL INT AUTO_INCREMENT PRIMARY KEY,
    URL VARCHAR(255) UNIQUE,
    Title VARCHAR(255),
    Description TEXT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Création de l'index sur la colonne URL dans la table URLInfo
CREATE INDEX idx_URLInfo_URL ON URLInfo (URL);

-- Création des tables pour les mots-clés (Mots_A, Mots_B, Mots_C, ...)
-- Ces tables seront créées dynamiquement au besoin.
