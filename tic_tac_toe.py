# Fonction de recherche d'index
def index_case_selectionnee(valeur, matrice):
    for x, ligne in enumerate(matrice):
        for y, element in enumerate(ligne):
            if element == valeur:
                return (x, y)
    return None

# Fonction pour afficher la grille
def afficher_grille(myDico):
    print("\nGrille de jeu :")
    for ligne in myDico:
        print("|".join(ligne))
        print("-" * 5)

# Fonction pour les tours de jeu
def tour(joueur, symbole, myDico, liste):
    while True:
        choix_case = input(f"\n{joueur}, donnez un numéro de case (1-9) : ")

        if choix_case not in liste:
            print("La valeur renseignée n'est pas valide, essayez à nouveau.")
            continue

        clef, valeur = index_case_selectionnee(choix_case, myDico)
        if clef is not None:
            myDico[clef][valeur] = symbole
            liste.remove(choix_case)
            break

    afficher_grille(myDico)
    return choix_victoire(joueur, myDico)

# Fonction déterminant les conditions de victoire
def choix_victoire(joueur, myDico):
    for ligne in myDico:
        if ligne[0] == ligne[1] == ligne[2] and ligne[0] != " ":
            print(f"\n{joueur}, vous avez gagné !! L'autre joueur paye l'apéro.")
            return True

    for colonne in range(3):
        if myDico[0][colonne] == myDico[1][colonne] == myDico[2][colonne] and myDico[0][colonne] != " ":
            print(f"\n{joueur}, vous avez gagné !! L'autre joueur paye l'apéro.")
            return True

    if (myDico[0][0] == myDico[1][1] == myDico[2][2] and myDico[0][0] != " ") or (myDico[0][2] == myDico[1][1] == myDico[2][0] and myDico[0][2] != " "):
        print(f"\n{joueur}, vous avez gagné !! L'autre joueur paye l'apéro.")
        return True

    return False

# Fonction de jeu
def morpion():
    myDico = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    liste = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    afficher_grille(myDico)

    while True:
        if tour("Joueur 1", "X", myDico, liste):
            break
        if tour("Joueur 2", "O", myDico, liste):
            break
        if not liste:
            print("\nMatch nul !")
            break

# Boucle de redémarrage
while True:
    morpion()
    relancer_partie = input("\nNouvelle partie ? (O/N) : ")
    if relancer_partie.upper() == "N":
        print("À bientôt !")
        break
