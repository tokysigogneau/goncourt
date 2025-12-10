# -*- coding: utf-8 -*-


from dataclasses import dataclass, field
from datetime import date

from daos.auteur_dao import AuteurDao
from daos.editeur_dao import EditeurDao
from daos.livre_dao import LivreDao
from daos.resultat_dao import  ResultatDao



from models.auteur import Auteur
from models.editeur import Editeur
from models.livre import Livre
from models.resultat import Resultat


@dataclass
class Goncourt:
    """Couche métier de l'application de gestion d'une école,
    reprenant les cas d'utilisation et les spécifications fonctionnelles :
    - courses : liste des cours existants
    - teachers : liste des enseignants
    - students : liste des élèves"""

    auteur: list[Auteur] = field(default_factory=list, init=False)
    editeur: list[Editeur] = field(default_factory=list, init=False)
    livre: list[Livre] = field(default_factory=list, init=False)
    resultat: list[Resultat] = field(default_factory=list, init=False)

    # teachers: list[Teacher] = field(default_factory=list, init=False)
    # students: list[Student] = field(default_factory=list, init=False)

    def add_auteur(self, auteur: Auteur) -> None:
        """Ajout du cours course à la liste des cours."""
        self.auteur.append(auteur)

    def add_editeur(self, editeur: Editeur) -> None:
        """Ajout du cours course à la liste éditeurs."""
        self.editeur.append(editeur)

    def add_livre(self, livre: Livre) -> None:
        """Ajout du cours course à la liste éditeurs."""
        self.livre.append(livre)

    def add_resultat(self, livre: Livre) -> None:
        """Ajout du cours course à la liste éditeurs."""
        self.livre.append(livre)


    #
    # def display_courses_list(self) -> None:
    #     """Affichage de la liste des cours avec pour chacun d'eux :
    #     - leur enseignant
    #     - la liste des élèves le suivant"""
    #     for course in self.courses:
    #         print(f"cours de {course}")
    #         for student in course.students_taking_it:
    #             print(f"- {student}")
    #         print()

    @staticmethod
    def get_auteur_by_id(id_auteur: int):
        auteur_dao: AuteurDao = AuteurDao()
        return auteur_dao.read(id_auteur)

    @staticmethod
    def get_editeur_by_id(id_editeur: int):
        editeur_dao: EditeurDao = EditeurDao()
        return editeur_dao.read(id_editeur)

    @staticmethod
    def get_livre_by_id(id_livre: int):
        livre_dao: LivreDao = LivreDao()
        return livre_dao.read(id_livre)

    @staticmethod
    def get_resultat_by_id(id_resultat: int):
        resultat_dao: ResultatDao = ResultatDao()
        return resultat_dao.read(id_resultat)

    @staticmethod
    def get_resultats_by_selection(r_numero_selection: int) -> list[Resultat]:
        resultat_dao = ResultatDao()
        return resultat_dao.read_selection(r_numero_selection)






