from business.goncourt import Goncourt

def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue au Goncourt 2025 !
--------------------------""")

    goncourt: Goncourt = Goncourt()
"""
    Ici on trouvera l'ensemble des commandes possibles à réaliser :
        - Afficher la description de chaque auteur, livre et éditeurs
        - Afficher les livres qui ont été qualifiés sur une selection choisie
        - Insérer un livre dans une séléction
        - Mettre à jour le nombre de votes obtenus par chaque livre dans une selection choisie
        - Revenir en arrière le 3 septembre ( supprimer les livres de la selection 2 et 3)

"""


    # ############ PRINT AUTEUR BY ID
    # print (goncourt.get_auteur_by_id(1))
    # print (goncourt.get_auteur_by_id(2))
    # print (goncourt.get_auteur_by_id(3))


    # ############ PRINT EDITEUR BY ID
    # print (goncourt.get_editeur_by_id(1))
    # print (goncourt.get_editeur_by_id(2))
    # print (goncourt.get_editeur_by_id(3))



    # # ############ PRINT LIVRE BY ID
    ### ID  livres de 31 à 45
    # print (goncourt.get_livre_by_id(31))
    # print(goncourt.get_livre_by_id(32))


    # # ############ PRINT RESULTAT BY ID
    # print (goncourt.get_resultat_by_id(1))


    # # # ############ PRINT RESULTAT BY SELECTION
    #
    # resultats = goncourt.get_resultats_by_selection(3)
    # for resultat in resultats:
    #     print(resultat)



    ################ TIME TRAVEL TO 3 SEPTEMBER
    # goncourt.delete_select(2)
    # goncourt.delete_select(3)


    # # # ############ INSERT UN LIVRE DANS UNE SELECTION
    ### ID  livres de 31 à 45
    # goncourt.insert_resultats_by_selection(3,0,42)
    # goncourt.insert_resultats_by_selection(3,0,43)
    # goncourt.insert_resultats_by_selection(3,0,44)

    # # # ############ AJOUTER UN NB DE VOTE A UN LIVRE DANS UNE SELECTION
    ### ID  livres de 31 à 45
    # goncourt.update_vote(3,3,42)





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

