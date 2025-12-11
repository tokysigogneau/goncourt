from __future__ import annotations
from abc import ABC
from dataclasses import field, dataclass
from typing import Optional, TYPE_CHECKING


if TYPE_CHECKING:
    from models.livre import Livre


@dataclass
class Resultat:
    """Résultats des votes et chaque tour"""

    r_numero_selection: int
    r_total_votes: Optional[int] = field(default=0)
    fk_id_livre: Optional[int] = field(default=None, init=False)
    id_resultat: Optional[int] = field(default=None, init=False)

    r_livre: Livre | None = field(default=None, init=False)


    def set_livre(self, livre: "Livre"):
        self.r_livre = livre

    def __str__(self) -> str:
        titre = self.r_livre.l_titre if self.r_livre else "Aucun livre"
        return (
            f"Selection numero : {self.r_numero_selection}\n"
            f"Total de votes : {self.r_total_votes}\n"
            
            f"Titre : << {self.r_livre.l_titre} >> écrit par {self.r_livre.l_auteur.a_nom} en {self.r_livre.l_date_de_parution} \n" +\
            f"Contient {self.r_livre.l_nb_page} pages, prix : {self.r_livre.l_prix} Code ISBN : {self.r_livre.l_isbn} \n" +\
            f"Biographie : {self.r_livre.l_auteur.a_biographie} \n" +\
            f"{self.r_livre.l_editeur}\n" +\
            f"-----------------------------------------------"

        )