#affichage du message de bienvenue
print("Bienvenue dans le jeu du morpion !")

#choix du mode de jeu
def choix_mode():
    mode = input("Voulez-vous jouer ou voir les scores ? (jouer/score) ")
    if mode == "jouer":
        mode = "jeu"
    elif mode == "score":
        mode = "info_score"
    else:
        print("Veuillez entrer une valeur valide.")
        choix_mode()
    return mode

#initialisation des variables
joueur1 = input("Joueur 1, entrez votre nom : ")
joueur2 = input("Joueur 2, entrez votre nom : ")
tour = 1
joueur = joueur1
grille = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
gagnant = False


#affichage des joueurs
def affichage_joueurs():
    print("Joueur 1 :", joueur1)
    print("Joueur 2 :", joueur2)

#affichage du plateau
def affichage_plateau(plateau):
    print("   0  1  2")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(plateau[i][j], end="  ")
        print()

#initialisation du plateau
plateau = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
#affichage du plateau
affichage_plateau(plateau)

#affichage des scores
def info_score():
    file = open("score.txt", "r")
    print(file.read())
    file.close()

#choix de la ligne
def choix_ligne():
    ligne = input("Choisissez une ligne : ")
    if ligne not in "012":
        print("Veuillez entrer une valeur valide.")
        choix_ligne()
    else:
        return int(ligne)

#choix de la colonne
def choix_colonne():
    colonne = input("Choisissez une colonne : ")
    if colonne not in "012":
        print("Veuillez entrer une valeur valide.")
        choix_colonne()
    else:
        return int(colonne)



#choix de la case
def choix_case(plateau):
    global tour
    case = input("Choisissez une case (ligne,colonne) : ")
    if case[0] not in "012" or case[2] not in "012":
        print("Veuillez entrer une valeur valide.")
        choix_case(plateau)
    elif plateau[int(case[0])][int(case[2])] != " ":
        print("Cette case est déjà prise.")
        choix_case(plateau)
    else:
        if tour % 2 == 1:
            plateau[int(case[0])][int(case[2])] = "X"
        else:
            plateau[int(case[0])][int(case[2])] = "O"

#score
def score(plateau):
    #vérification des lignes
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2] and plateau[i][0] != " ":
            return plateau[i][0]
    #vérification des colonnes
    for j in range(3):
        if plateau[0][j] == plateau[1][j] == plateau[2][j] and plateau[0][j] != " ":
            return plateau[0][j]
    #vérification des diagonales
    if plateau[0][0] == plateau[1][1] == plateau[2][2] and plateau[0][0] != " ":
        return plateau[0][0]
    if plateau[0][2] == plateau[1][1] == plateau[2][0] and plateau[0][2] != " ":
        return plateau[0][2]
    return " "


#jeu
def jeu():
    global tour
    global joueur
    global gagnant
    while tour <= 9 and gagnant == False:
        affichage_plateau(plateau)
        print("C'est au tour de", joueur)
        choix_case(plateau)
        if score(plateau) == joueur1:
            print(joueur1, "a gagné !")
            gagnant = True
        elif score(plateau) == joueur2:
            print(joueur2, "a gagné !")
            gagnant = True
        elif tour == 9:
            print("Match nul !")
        if joueur == joueur1:
            joueur = joueur2
        else:
            joueur = joueur1
        tour += 1

#initialisation du jeu
def init():
    mode = choix_mode()
    if mode == "jeu":
        affichage_joueurs()
        jeu()
    elif mode == "info_score":
        info_score()

init()





#programme principal
mode = choix_mode()
if mode == "jeu":
    jeu()
    file = open("score.txt", "a")
    file.write(joueur + " a gagné !")
    file.close()
elif mode == "info_score":
    info_score()


#victoire
def victoire(plateau):
    if score(plateau) == joueur1:
        print(joueur1, "a gagné !")
        file = open("score.txt", "a")
        file.write(joueur1 + " a gagné !")
        file.close()
    elif score(plateau) == joueur2:
        print(joueur2, "a gagné !")
        file = open("score.txt", "a")
        file.write(joueur2 + " a gagné !")
        file.close()
    elif tour == 9:
        print("Match nul !")
        file = open("score.txt", "a")
        file.write("Match nul !")
        file.close()
    else:
        return False
    return True





#affichage du message de fin
print("Fin du jeu.")

