-- Créer la base de données
CREATE DATABASE IF NOT EXISTS store;

-- Utiliser la base de données
USE store;

-- Créer la table "category"
CREATE TABLE IF NOT EXISTS category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Créer la table "product"
CREATE TABLE IF NOT EXISTS product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price INT,
    quantity INT,
    id_category INT,
    FOREIGN KEY (id_category) REFERENCES category(id)
);

-- Insérer des catégories
INSERT INTO category (name) VALUES ('Électronique');
INSERT INTO category (name) VALUES ('Vêtements');
INSERT INTO category (name) VALUES ('Alimentation');

-- Insérer des produits
INSERT INTO product (name, description, price, quantity, id_category) VALUES ('Smartphone', 'Téléphone intelligent', 500, 10, 1);
INSERT INTO product (name, description, price, quantity, id_category) VALUES ('T-shirt', 'T-shirt en coton', 20, 50, 2);
INSERT INTO product (name, description, price, quantity, id_category) VALUES ('Pommes', 'Pommes rouges', 2, 100, 3);
