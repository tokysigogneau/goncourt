# -*- coding: utf-8 -*-

"""
Classe Livre
"""

# pour simplifier les annotations de types des classes non importées à l'exécution
# (teacher: Teacher plutôt que teacher: 'Teacher')
from __future__ import annotations

from typing import Optional, TYPE_CHECKING
from dataclasses import dataclass, field
from datetime import date



from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.editeur import  Editeur
from models.auteur import Auteur


@dataclass
class Livre:
    """Cours enseigné à l'école :
    - id_livre : clé primaire de l'entité Livre
    - l_titre : titre du livre
    - l_date_de_parution : date de publication
    - l_nb_page : nombre de pages du livre
    - l_prix : prix du livre
    - l_isbn : code de référence du livre
    - l_auteur : l'auteur du livre
    - l_editeur : l'éditeur du livre

    """
    id_livre: Optional[int] = field(default=None, init=False)
    l_titre: str
    l_date_de_parution : date
    l_nb_page : int
    l_prix : float
    l_isbn : int
    l_auteur : Auteur | None = field(default=None, init=False)
    l_editeur : Editeur | None = field(default=None, init=False)

    def set_auteur(self, auteur: Auteur):
        self.l_auteur = auteur

    def set_editeur(self, editeur: Editeur):
        self.l_editeur = editeur



    def __str__(self) -> str:
        return f"Titre : << {self.l_titre} >> écrit par {self.l_auteur.a_nom} en {self.l_date_de_parution} \n" +\
            f"Contient {self.l_nb_page} pages, prix : {self.l_prix} Code ISBN : {self.l_isbn} \n" +\
            f"Biographie : {self.l_auteur.a_biographie} \n" +\
            f"{self.l_editeur}" +\
            f" \n ---------------------------------------------"

