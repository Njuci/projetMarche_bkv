
create database if not exists b_marche;
use b_marche;
drop table if exists tb_produit;
drop table if exists tb_commande;
drop table if exists tb_categorie;
drop table if exists tb_livraison;
drop table if exists tb_boutique;
drop table if exists tb_utilisateur;
create table if not exists tb_utilisateur(
    username varchar(50) primary key not null,
    nom varchar(50),
    prenom varchar(50),
    email varchar(50) unique not null,
    password varchar(50),
    role enum('vendeur', 'acheteur') not null,
    adresse varchar(50),
    telephone varchar(50),
    unique key(nom, prenom)
);
CREATE TABLE IF NOT EXISTS tb_categorie(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_boutique(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(50) UNIQUE NOT NULL,
    id_vendeur VARCHAR(50) NOT NULL,
    FOREIGN KEY(id_vendeur) REFERENCES tb_utilisateur(username) ON DELETE CASCADE
);
DELIMITER $$
CREATE TRIGGER check_vendeur_before_insert
BEFORE INSERT ON tb_boutique
FOR EACH ROW
BEGIN
    DECLARE user_role VARCHAR(50);
    SELECT role INTO user_role FROM tb_utilisateur WHERE username = NEW.id_vendeur;
    IF user_role <> 'vendeur' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Seuls les vendeurs peuvent avoir une boutique.';
    END IF;
END$$
DELIMITER ;
-- create tb_produit
create table if not exists tb_produit(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(50) NOT NULL,
    prix DECIMAL(10, 2) NOT NULL,
    
    id_categorie INT NOT NULL,
    id_boutique INT NOT NULL,
    FOREIGN KEY(id_categorie) REFERENCES tb_categorie(id) ON DELETE CASCADE,
    FOREIGN KEY(id_boutique) REFERENCES tb_boutique(id) ON DELETE CASCADE
);

-- create tb_commande
create table if not exists tb_commande(
    id INT PRIMARY KEY AUTO_INCREMENT,
    date_commande DATE NOT NULL,
    id_utilisateur VARCHAR(50) NOT NULL,    
    id_produit INT NOT NULL,
    quantite INT NOT NULL,
    paye BOOLEAN NOT NULL ,
    FOREIGN KEY(id_produit) REFERENCES tb_produit(id) ON DELETE CASCADE,

    FOREIGN KEY(id_utilisateur) REFERENCES tb_utilisateur(username) ON DELETE CASCADE
);!!!!
DELIMITER $$
CREATE TRIGGER check_acheteur_before_insert
BEFORE INSERT ON tb_commande
FOR EACH ROW
BEGIN
    DECLARE user_role VARCHAR(50);
    SELECT role INTO user_role FROM tb_utilisateur WHERE username = NEW.id_utilisateur;
    IF user_role <> 'client' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Seuls les acheteurs peuvent passer une commande.';
    END IF;
END$$
DELIMITER ;
create table if not exists tb_livraison(
    date_livraison DATE NOT NULL,
    id_commande INT UNIQUE NOT NULL,
    montant DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY(id_commande) REFERENCES tb_commande(id) ON DELETE CASCADE
);
