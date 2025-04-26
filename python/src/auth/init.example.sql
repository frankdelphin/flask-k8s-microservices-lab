-- init.sql

DROP DATABASE IF EXISTS ` <DB_NAME>`;
DROP USER IF EXISTS '<DB_USER>'@'localhost';

CREATE DATABASE ` <DB_NAME>`;

CREATE USER '<DB_USER>'@'localhost' IDENTIFIED BY '<DB_PASSWORD>';

GRANT ALL PRIVILEGES ON ` <DB_NAME>`.* TO '<DB_USER>'@'localhost';

FLUSH PRIVILEGES;

USE ` <DB_NAME>`;

CREATE TABLE IF NOT EXISTS `user` (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    email VARCHAR(255) NOT NULL UNIQUE, 
    password VARCHAR(255) NOT NULL
);

-- Insère un utilisateur test
INSERT INTO `user` (email, password) 
VALUES ('admin@mail.com', 'admin123');


-- RUN it in cmd with : `mysql -uroot -p < init.sql`