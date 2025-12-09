CREATE TABLE IF NOT EXISTS resultat (
    id_resultat INT NOT NULL AUTO_INCREMENT,
    r_numero_selection INT(10),
    r_total_votes INT(10),
    id_livre INT NOT NULL,
    PRIMARY KEY (id_resultat)
) ENGINE=InnoDB;


CREATE TABLE IF NOT EXISTS livre (
    id_livre INT NOT NULL AUTO_INCREMENT,
    l_titre INT(10),
    l_date_de_parution DATE,
    l_nb_page INT(10),
    PRIMARY KEY (id_livre)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS personnages_principaux (
    id_perso_p INT NOT NULL AUTO_INCREMENT,
    pp_nom VARCHAR(20),
    PRIMARY KEY (id_perso_p)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS auteur (
    id_auteur INT NOT NULL AUTO_INCREMENT,
    a_nom VARCHAR(20),
    a_biographie VARCHAR(255),
    PRIMARY KEY (id_auteur)
) ENGINE=InnoDB;


CREATE TABLE IF NOT EXISTS editeur (
    id_editeur INT NOT NULL AUTO_INCREMENT,
    e_nom VARCHAR(20),
    e_prix DECIMAL(6,2),
    e_ISBN INT (10),
    PRIMARY KEY (id_editeur)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS jury (
    id_jury INT NOT NULL AUTO_INCREMENT,
    j_nom VARCHAR(20),
    j_role VARCHAR(20),
    PRIMARY KEY (id_jury)
) ENGINE=InnoDB;


CREATE TABLE IF NOT EXISTS selectionner (
    id_select INT NOT NULL AUTO_INCREMENT,
    fk_id_livre INT NOT NULL,
    fk_id_jury INT NOT NULL,

    PRIMARY KEY (id_select),
    FOREIGN KEY (fk_id_livre) REFERENCES livre(id_livre)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (fk_id_jury) REFERENCES jury(id_jury)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;



'ALTER TABLES FK'


ALTER TABLE resultat 
    ADD fk_id_livre INT (10),
	ADD FOREIGN KEY (fk_id_livre) REFERENCES livre(id_livre)
	
ALTER TABLE personnages_principaux 
    ADD fk_id_livre INT (10),
	ADD FOREIGN KEY (fk_id_livre) REFERENCES livre(id_livre);
	
ALTER TABLE livre
    ADD fk_id_editeur INT (10),
    ADD fk_id_auteur INT (10),
	ADD FOREIGN KEY (fk_id_editeur) REFERENCES editeur(id_editeur),
    ADD FOREIGN KEY (fk_id_auteur) REFERENCES auteur(id_auteur);
