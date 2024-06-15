CREATE DATABASE IF NOT EXISTS elgoog;
USE elgoog;

CREATE TABLE IF NOT EXISTS `groups` (
    id_group INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    members JSON
)ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS urls (
    id_url INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) UNIQUE,
    keywords JSON,
    description TEXT,
    title VARCHAR(100),
    banned BOOLEAN DEFAULT FALSE,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (timestamp)
)ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS url_info (
    id_info INT AUTO_INCREMENT PRIMARY KEY,
    id_url INT,
    url VARCHAR(255),
    description TEXT,
    title VARCHAR(255),
    banned BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_url) REFERENCES urls(id_url) ON DELETE CASCADE
)ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


CREATE DATABASE IF NOT EXISTS elgoog_users;
USE elgoog_users;


CREATE TABLE `users` (
  `id` int NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



-- init.sql

CREATE USER IF NOT EXISTS 'backenduser'@'%' IDENTIFIED BY 'backendpassword';
GRANT SELECT ON elgoog.* TO 'backenduser'@'%';
GRANT SELECT ON elgoog_users.* TO 'backenduser'@'%';

CREATE USER IF NOT EXISTS 'crawleruser'@'%' IDENTIFIED BY 'crawlerpassword';
GRANT SELECT, INSERT, UPDATE, DELETE ON elgoog.* TO 'crawleruser'@'%';

CREATE USER IF NOT EXISTS 'adminuser'@'%' IDENTIFIED BY 'zasaqu357';
GRANT ALL PRIVILEGES ON *.* TO 'adminuser'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;
