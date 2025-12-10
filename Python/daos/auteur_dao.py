from models.auteur import Auteur
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class AuteurDao(Dao[Auteur]):
    def create(self, auteur: Auteur) -> int:

        ...
        return True

    def read(self, id_auteur: int) -> Optional[Auteur]:
        """Renvoit l'auteur qui correspond à l'ID
           (ou None s'il n'a pu être trouvé)"""
        auteur: Optional[Auteur]

        with Dao.connection.cursor() as cursor:
            sql = "SELECT a_nom, a_biographie FROM auteur WHERE id_auteur=%s"
            cursor.execute(sql, (id_auteur,))
            record = cursor.fetchone()
        if record is not None:
            auteur = Auteur(record['a_nom'], record['a_biographie'])

        else:
            auteur = None

        return auteur

    def update(self, auteur: Auteur) -> bool:

        ...
        return True

    def delete(self, auteur: Auteur) -> bool:

        ...
        return True

