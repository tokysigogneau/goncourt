from models.resultat import Resultat
from models.auteur import Auteur
from models.editeur import Editeur
from models.livre import Livre

from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class ResultatDao(Dao[Resultat]):
    def create(self, r_numero_selection: int, r_total_votes: int, fk_id_livre: int) -> Optional[Resultat]:

        with Dao.connection.cursor() as cursor:
            sql = """
                INSERT INTO resultat (r_numero_selection, r_total_votes, fk_id_livre)
                VALUES (%s, %s, %s);
            """
            cursor.execute(sql, (r_numero_selection, r_total_votes, fk_id_livre))

            Dao.connection.commit()

            print(f"Les valeurs ont bien été insérées dans la BDD : \n" + \
                  f"Numéro de selection : {r_numero_selection} " + \
                  f"Total votes : {r_total_votes}   Livre numéro : {fk_id_livre} \n")

        return True


    ############### READ BY ID

    def read(self, id_resultat: int) -> Optional[Resultat]:
        """Renvoit le resultat qui correspond à la selection choisie
           (ou None s'il n'a pu être trouvé)"""
        resultat: Optional[Resultat]

        with Dao.connection.cursor() as cursor:
            sql = """
            
                SELECT 
                    r_numero_selection,
                    r_total_votes,
                    fk_id_livre,
                    livre.l_titre,
                    livre.l_date_de_parution,
                    livre.l_nb_page,
                    livre.l_prix,
                    livre.l_isbn,
                    auteur.a_nom,
                    auteur.a_biographie,
                    editeur.e_nom
                FROM resultat
                INNER JOIN livre ON livre.id_livre = resultat.fk_id_livre
                INNER JOIN editeur ON editeur.id_editeur = livre.fk_id_editeur
                INNER JOIN auteur ON auteur.id_auteur = livre.fk_id_auteur
                WHERE resultat.id_resultat = %s;
           
            """
            cursor.execute(sql, (id_resultat,))
            record = cursor.fetchone()

        if record is not None:
            auteur = Auteur(
                a_nom=record["a_nom"],
                a_biographie=record["a_biographie"]
            )

            editeur = Editeur(
                e_nom=record["e_nom"]
            )

            livre = Livre(
                l_titre=record["l_titre"],
                l_date_de_parution=record["l_date_de_parution"],
                l_nb_page=record["l_nb_page"],
                l_prix=record["l_prix"],
                l_isbn=record["l_isbn"]
            )
            livre.set_auteur(auteur)
            livre.set_editeur(editeur)

            resultat = Resultat(
                r_numero_selection=record["r_numero_selection"],
                r_total_votes=record["r_total_votes"]
            )
            resultat.set_livre(livre)

        else:
            resultat = None

        return resultat

    ############### READ BY SELECTION NUMBER

    def read_selection(self, r_numero_selection: int) -> Optional[Resultat]:
        """Renvoit le resultat qui correspond à la selection choisie
           (ou None s'il n'a pu être trouvé)"""

        #list qui contient les auteurs et livres
        resultats: list[Resultat] = []

        with Dao.connection.cursor() as cursor:
            sql = """

                SELECT 
                    r_numero_selection,
                    r_total_votes,
                    fk_id_livre,
                    livre.l_titre,
                    livre.l_date_de_parution,
                    livre.l_nb_page,
                    livre.l_prix,
                    livre.l_isbn,
                    auteur.a_nom,
                    auteur.a_biographie,
                    editeur.e_nom
                FROM resultat
                INNER JOIN livre ON livre.id_livre = resultat.fk_id_livre
                INNER JOIN editeur ON editeur.id_editeur = livre.fk_id_editeur
                INNER JOIN auteur ON auteur.id_auteur = livre.fk_id_auteur
                WHERE resultat.r_numero_selection = %s;

            """
            cursor.execute(sql, (r_numero_selection,))
            records = cursor.fetchall()
        if records is not None:
            #We create each object that will contain the Resultat in the list
            for record in records:

                auteur = Auteur(
                    a_nom=record["a_nom"],
                    a_biographie=record["a_biographie"]
                )

                editeur = Editeur(
                    e_nom=record["e_nom"]
                )

                livre = Livre(
                    l_titre=record["l_titre"],
                    l_date_de_parution=record["l_date_de_parution"],
                    l_nb_page=record["l_nb_page"],
                    l_prix=record["l_prix"],
                    l_isbn=record["l_isbn"]
                )

                #this link the objects to the big object Resultat
                livre.set_auteur(auteur)
                livre.set_editeur(editeur)

                resultat = Resultat(
                    r_numero_selection=record["r_numero_selection"],
                    r_total_votes=record["r_total_votes"]
                )
                resultat.set_livre(livre)

                resultats.append(resultat)

        else:
            resultats = None

        return resultats

    def update(self, r_numero_selection: int, r_total_votes: int, fk_id_livre: int) -> Optional[Resultat]:

        with Dao.connection.cursor() as cursor:
            sql = """
                UPDATE resultat 
                SET r_total_votes=%s
                WHERE r_numero_selection = %s AND fk_id_livre = %s; 
            """
            cursor.execute(sql, (r_total_votes, r_numero_selection,  fk_id_livre))

            Dao.connection.commit()

            print(f"Le total de votes a bien été mis à jour : \n" + \
                  f"Numéro de selection : {r_numero_selection} " + \
                  f"Total votes : {r_total_votes}   Livre numéro : {fk_id_livre} \n")

        return True

    def delete(self, r_numero_selection: int) -> bool:

        with Dao.connection.cursor() as cursor:
            sql = """
                DELETE 
                FROM resultat 
                WHERE r_numero_selection = %s; 
            """
            cursor.execute(sql, (r_numero_selection))

            Dao.connection.commit()

            print (f"Les données de la selection {r_numero_selection} ont bien été retirés \n" )

        return True

