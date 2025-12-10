from business.goncourt import Goncourt

def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue au Goncourt 2025 !
--------------------------""")

    goncourt: Goncourt = Goncourt()

    # initialisation d'un ensemble de cours, enseignants et élèves composant l'école

    # # affichage de la liste des cours, leur enseignant et leurs élèves
    # school.display_courses_list()

    # print(school.get_course_by_id(1))
    # print(school.get_course_by_id(2))
    # print(school.get_course_by_id(9))
    # print()

    # ############ PRINT AUTEUR BY ID
    # print (goncourt.get_auteur_by_id(1))
    # print (goncourt.get_auteur_by_id(2))
    # print (goncourt.get_auteur_by_id(3))


    # ############ PRINT EDITEUR BY ID
    # print (goncourt.get_editeur_by_id(1))
    # print (goncourt.get_editeur_by_id(2))
    # print (goncourt.get_editeur_by_id(3))



    # # ############ PRINT LIVRE BY ID
    # print (goncourt.get_livre_by_id(31))
    # print(goncourt.get_livre_by_id(32))


    # # # ############ PRINT RESULTAT BY ID
    # print (goncourt.get_resultat_by_id(1))


    # # ############ PRINT RESULTAT BY SELECTION

    resultats = goncourt.get_resultats_by_selection(3)
    for resultat in resultats:
        print(resultat)





    # print("///////////// TEST READ ALL")
    #
    #
    # student_list = school.get_student_all()
    #
    # for student in student_list:
    #     print(f"{student.first_name} {student.last_name} {student.age}")
    #


if __name__ == '__main__':
    main()

