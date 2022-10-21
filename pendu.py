#affichage du message de bienvenue
print("Bienvenue dans le jeu du pendu !")
#affichage du message
print("Vous devez deviner un mot en 8 coups maximum.")
#affichage du message
print("Vous pouvez proposer une lettre à chaque tour.")
#affichage du message
print("Si la lettre est dans le mot, elle sera affichée.")
#affichage du message
print("Si la lettre n'est pas dans le mot, vous perdez un essai.")
#affichage du message
print("Si vous utilisez tous vos essais... vous avez perdu.")
#affichage du message
print("Bonne chance !")


#affichage du mot à trouver
from random import*
fichier = open("dico_france.txt", "r", encoding= "iso 8859-1 ") #récupèration du fichier dictionnaire dico france (répertoire local ou le fichier en consigné)
liste_mots = fichier.readlines()    # met tous les mots du fichiers dico.txt dans une liste
mot = choice(liste_mots)            # prend au hasard un mot dans la liste
mot = mot.rstrip()                  # supprime le caractère "saut à la ligne"
fichier.close()
mot_devine = "-" * len(mot)         # crée un mot de même longueur avec des "-" à la place des lettres
print(mot_devine)                   # affiche le mot à deviner

#choix du niveau de difficulté
def niv():
    niveau = input("Choisissez un niveau de difficulté : facile, moyen ou difficile :")
    while niveau != "facile" and niveau != "moyen" and niveau != "difficile":
        print("Vous devez choisir un niveau de difficulté.")
        niveau = input("Choisissez un niveau de difficulté :")
    if niveau == "facile":
        essais = 8
    elif niveau == "moyen":
        essais = 6
    else:
        essais = 4
    return essais, niveau

#vérification de la saisie de l'utilisateur
def saisie_utilisateur():
    saisie = input("Veuillez saisir une lettre :")
    while len(saisie) != 1:
        print("Vous devez saisir une seule lettre.")
        saisie = input("Veuillez saisir une lettre :")
    return saisie

#affichage du nombre d'essais restants
def affichage_essais(essais):
    if essais == 1:
        print("Il vous reste 1 essai.")
    else:
        print("Il vous reste", essais, "essais.")

#boucle principale
essais, niveau = niv()
affichage_essais(essais)
liste=[]
if niveau!="difficile":
    #boucle jeu
    while essais > 0:
        lettre = saisie_utilisateur()
        liste.append(lettre) #ajout de la lettre saisie dans la liste

        if lettre in mot:
            print("La lettre", lettre, "est dans le mot.")
            for i in range(len(mot)):
                if mot[i] == lettre:
                    mot_devine = mot_devine[:i] + lettre + mot_devine[i+1:]
            
        else:
            print("La lettre", lettre, "n'est pas dans le mot.")
            essais -= 1
        affichage_essais(essais)
        print(liste)
        print(mot_devine)

        #boucle victoire
        if mot == mot_devine:
            print("Bravo, vous avez gagné !")
            break
else :
    while essais > 0:
        lettre = saisie_utilisateur()
        liste.append(lettre) #ajout de la lettre saisie dans la liste
        if lettre in mot:
            print("La lettre", lettre, "est dans le mot.")
            for i in range(len(mot)):
                if mot[i] == lettre:
                    mot_devine = mot_devine[:i] + lettre + mot_devine[i+1:]
            
        else:
            print("La lettre", lettre, "n'est pas dans le mot.")
            essais -= 1
        affichage_essais(essais)
        print(mot_devine)
        if mot == mot_devine:
            print("Bravo, vous avez gagné !")
            break


if essais == 0:
    print("Vous avez perdu.")
    print("Le mot était", mot)
    #rejouer
    rejouer = input("Voulez-vous rejouer ? (o/n)")
    while rejouer != "o" and rejouer != "n":
        print("Vous devez répondre par o ou n.")
    
    if rejouer == "o":
        #boucle principale
        essais, niveau = niv()
        affichage_essais(essais)
        liste=[]
        if niveau!="difficile":
            #boucle jeu
            while essais > 0:
                lettre = saisie_utilisateur()
                liste.append(lettre) #ajout de la lettre saisie dans la liste

                if lettre in mot:
                    print("La lettre", lettre, "est dans le mot.")
                    for i in range(len(mot)):
                        if mot[i] == lettre:
                            mot_devine = mot_devine[:i] + lettre + mot_devine[i+1:]
                    
                else:
                    print("La lettre", lettre, "n'est pas dans le mot.")
                    essais -= 1
                affichage_essais(essais)
                print(liste)
                print(mot_devine)

                #boucle victoire
                if mot == mot_devine:
                    print("Bravo, vous avez gagné !")
                    break
        else :
            while essais > 0:
                lettre = saisie_utilisateur()
                liste.append(lettre) #ajout de la lettre saisie dans la liste
                if lettre in mot:
                    print("La lettre", lettre, "est dans le mot.")
                    for i in range(len(mot)):
                        if mot[i] == lettre:
                            mot_devine = mot_devine[:i] + lettre + mot_devine[i+1:]
                    
                else:
                    print("La lettre", lettre, "n'est pas dans le mot.")
                    essais -= 1
                affichage_essais(essais)
                print(mot_devine)
                if mot == mot_devine:
                    print("Bravo, vous avez gagné !")
                    break
    else:
        print("Merci d'avoir joué au jeu du pendu !")


#affichage du message de fin
print("Merci d'avoir joué au jeu du pendu !")


