from models.editeur import Editeur
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class EditeurDao(Dao[Editeur]):
    def create(self, editeur: Editeur) -> int:

        ...
        return True

    def read(self, id_editeur: int) -> Optional[Editeur]:
        """Renvoit l'editeur qui correspond à l'ID
           (ou None s'il n'a pu être trouvé)"""
        editeur: Optional[Editeur]

        with Dao.connection.cursor() as cursor:
            sql = """
            SELECT e_nom 
            FROM editeur 
            WHERE id_editeur=%s
            """
            cursor.execute(sql, (id_editeur,))
            record = cursor.fetchone()
        if record is not None:
            editeur = Editeur(record['e_nom'])

        else:
            editeur = None

        return editeur

    def update(self, editeur: Editeur) -> bool:

        ...
        return True

    def delete(self, editeur: Editeur) -> bool:

        ...
        return True

