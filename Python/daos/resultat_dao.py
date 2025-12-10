from models.resultat import Resultat
from models.auteur import Auteur
from models.editeur import Editeur
from models.livre import Livre

from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class ResultatDao(Dao[Resultat]):
    def create(self, resultat: Resultat) -> int:

        ...
        return True

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
            resultat = Resultat(record['a_nom'], record['a_biographie'])

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

    def update(self, resultat: Resultat) -> bool:

        ...
        return True

    def delete(self, resultat: Resultat) -> bool:

        ...
        return True

