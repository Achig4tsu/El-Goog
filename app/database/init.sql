CREATE DATABASE IF NOT EXISTS elgoog;

USE elgoog;

CREATE TABLE IF NOT EXISTS `groups` (
    id_group INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    members JSON
);

CREATE TABLE IF NOT EXISTS urls (
    id_url INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) UNIQUE,
    keywords JSON,
    description TEXT,
    title VARCHAR(100),
    banned BOOLEAN DEFAULT FALSE,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (timestamp)
);

CREATE TABLE IF NOT EXISTS url_info (
    id_info INT AUTO_INCREMENT PRIMARY KEY,
    id_url INT,
    url VARCHAR(255),
    description TEXT,
    title VARCHAR(255),
    banned BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_url) REFERENCES urls(id_url) ON DELETE CASCADE
);
