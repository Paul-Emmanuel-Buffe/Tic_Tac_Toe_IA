import random

def index_case_selectionnee(valeur, matrice):
    """Find the index of a value in a matrix."""
    for x, ligne in enumerate(matrice):
        for y, element in enumerate(ligne):
            if element == valeur:
                return (x, y)
    return None

def afficher_grille(myDico):
    """Display the game grid."""
    print("\nGame Grid:")
    print("-----")
    for ligne in myDico:
        print("|".join(ligne))
        print("-----")

def tour_joueur(joueur, symbole, myDico, liste):
    """Handle the player's turn."""
    while True:
        choix_case = input(f"\n{joueur} (Symbol: {symbole}), choose a number (1-9): ")

        if choix_case not in liste:
            print("Invalid input or spot taken. Try again.")
            continue

        clef, valeur = index_case_selectionnee(choix_case, myDico)
        if clef is not None:
            myDico[clef][valeur] = symbole
            liste.remove(choix_case)
            break

    afficher_grille(myDico)
    return choix_victoire(joueur, myDico)

def tour_ia(symbole, myDico, liste):
    """Handle the AI's turn."""
    print("\nAI's turn...")
    choix_case = random.choice(liste)
    clef, valeur = index_case_selectionnee(choix_case, myDico)

    if clef is not None:
        myDico[clef][valeur] = symbole
        liste.remove(choix_case)

    afficher_grille(myDico)
    return choix_victoire("AI", myDico)

def choix_victoire(joueur, myDico):
    """Check for a winning condition."""
    for ligne in myDico:
        if ligne[0] == ligne[1] == ligne[2] and ligne[0] != " ":
            print(f"\n{joueur}, you have won!!")
            return True

    for colonne in range(3):
        if myDico[0][colonne] == myDico[1][colonne] == myDico[2][colonne] and myDico[0][colonne] != " ":
            print(f"\n{joueur}, you have won!!")
            return True

    if (myDico[0][0] == myDico[1][1] == myDico[2][2] and myDico[0][0] != " ") or (myDico[0][2] == myDico[1][1] == myDico[2][0] and myDico[0][2] != " "):
        print(f"\n{joueur}, you have won!!")
        return True

    return False

def morpion():
    """Main function to run the Tic Tac Toe game."""
    myDico = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    liste = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    print("\nWelcome to Tic Tac Toe against AI!")
    afficher_grille(myDico)

    while True:
        if tour_joueur("Player 1", "X", myDico, liste):
            break
        if tour_ia("O", myDico, liste):
            break
        if not liste:
            print("\nIt's a draw!")
            break

while True:
    morpion()
    relancer_partie = input("\nDo you want to play a new game? (Y/N): ")
    if relancer_partie.upper() == "N":
        print("See you next time!")
        break

