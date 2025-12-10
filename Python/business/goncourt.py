# -*- coding: utf-8 -*-


from dataclasses import dataclass, field
from datetime import date

from daos.auteur_dao import AuteurDao
from daos.editeur_dao import EditeurDao



from models.auteur import Auteur
from models.editeur import Editeur



@dataclass
class Goncourt:
    """Couche métier de l'application de gestion d'une école,
    reprenant les cas d'utilisation et les spécifications fonctionnelles :
    - courses : liste des cours existants
    - teachers : liste des enseignants
    - students : liste des élèves"""

    auteur: list[Auteur] = field(default_factory=list, init=False)
    editeur: list[Editeur] = field(default_factory=list, init=False)
    # teachers: list[Teacher] = field(default_factory=list, init=False)
    # students: list[Student] = field(default_factory=list, init=False)

    def add_auteur(self, auteur: Auteur) -> None:
        """Ajout du cours course à la liste des cours."""
        self.auteur.append(auteur)

    def add_editeur(self, editeur: Editeur) -> None:
        """Ajout du cours course à la liste éditeurs."""
        self.editeur.append(editeur)


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

    # @staticmethod
    # def get_student_by_id(id_student: int):
    #     student_dao: StudentDao = StudentDao()
    #     return student_dao.read(id_student)
    #
    # @staticmethod
    # def get_student_all():
    #     student_list = StudentDao()
    #     return student_list.read_all()
    #
    # @staticmethod
    # def get_address_by_id(id_address: int):
    #     address_dao: AddressDao = AddressDao()
    #     return address_dao.read(id_address)
    #
    # @staticmethod
    # def get_teacher_by_id(id_teacher: int):
    #     teacher_dao: TeacherDao = TeacherDao()
    #     return teacher_dao.read(id_teacher)



