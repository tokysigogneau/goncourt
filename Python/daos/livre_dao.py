from models.auteur import Auteur
from models.editeur import Editeur
from models.livre import Livre
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class LivreDao(Dao[Livre]):
    def create(self, livre: Livre) -> int:

        ...
        return True

    def read(self, id_livre: int) -> Optional[Livre]:
        """Renvoie le livre correspondant à l'ID (ou None)"""

        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT 
                    l.l_titre,
                    l.l_date_de_parution,
                    l.l_nb_page,
                    l.l_prix,
                    l.l_isbn,
                    a.a_nom,
                    a.a_biographie,
                    e.e_nom
                FROM livre l
                INNER JOIN editeur e ON e.id_editeur = l.fk_id_editeur
                INNER JOIN auteur a ON a.id_auteur = l.fk_id_auteur
                WHERE l.id_livre = %s;
            """
            cursor.execute(sql, (id_livre,))
            record = cursor.fetchone()

        if record is None:
            return None

        # We create each object that will contain the Livre in the list
        livre = Livre(
            record['l_titre'],
            record['l_date_de_parution'],
            record['l_nb_page'],
            record['l_prix'],
            record['l_isbn']
        )

        # Object Auteur
        auteur = Auteur(
            a_nom=record['a_nom'],
            a_biographie=record['a_biographie']
        )

        # Object Editeur
        editeur = Editeur(
            e_nom=record['e_nom']
        )
        # this link the objects to the big object Livre
        livre.set_auteur(auteur)
        livre.set_editeur(editeur)

        return livre

    def update(self, livre: Livre) -> bool:

        ...
        return True

    def delete(self, livre: Livre) -> bool:

        ...
        return True

