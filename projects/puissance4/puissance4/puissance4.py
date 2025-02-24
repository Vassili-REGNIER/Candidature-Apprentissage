import random
import time

def nouvelle_grille():
    """Renvoie une grille (matrice) de 8 par 10 contenant que des 0 (8 lignes, 10 colonnes)
    """
    
    # Génération d'une liste de 8 sous-listes de 10 éléments 0 par compréhension
    grille_vide = [[0 for i in range(10)] for j in range(8)]
    return grille_vide

def affiche(grille):
    """Affiche l'interface d'une grille de manière adaptée au jeu puissance 4
    """

    # Affichage du haut de l'interface
    print(
        "-------------------------------------------------------------\n"
        "|          O~~~~~~~~0    PUISSANCE  4    O~~~~~~~O          |\n"
        "-------------------------------------------------------------\n", end=""
    )
    
    # Pour chaque case, on remplace le numéro du joueur par son symbole en ajoutant des traits de séparations
    for colonne in grille:        
        for case in colonne:
            print("| ", end="")

            if case == 0:
                print(" .  ", end = "")
            elif case == 1:
                print(" X  ", end = "")
            elif case == 2:
                print(" O  ", end = "")
            else:
                print(" ", chr(164), "  ", sep="", end="")

        print("|")

    # Affichage du bas de l'interface
    print(
        "-------------------------------------------------------------\n"
        "|  1     2     3     4     5     6     7     8     9    10  |\n"
        "-------------------------------------------------------------\n", end=""
    )

def test_coup_possible(grille, colonne):
    """Renvoie vrai si la colonne d'une grille ne contient pas uniquement des 0, renvoie faux sinon
    """

    # Changement du numéro de la colonne à son rang
    colonne -= 1
    
    # Renvoie vrai si la case la plus haute de la colonne contient 0, sinon, renvoie faux
    if grille[0][colonne] == 0:            
        return True
    return False

def jou(grille, joueur, colonne):
    """Place un jeton (numéro du joueur) sur une grille, à la case vide (un 0) la plus basse d'une colonne.
    """

    # Changement du numéro de la colonne à son rang et extraction de chaque élément de la colonne
    colonne -= 1
    element_colonne = [grille[i][colonne] for i in range(8)]

    # Parcours de chaque élément de la colonne et remplace la première case vide (contenant 0) par le jeton du joueur (numéro du joueur)
    for ligne in range(7, -1, -1):
        if element_colonne[ligne] == 0:
            grille[ligne][colonne] = joueur
            return

def horizontal(grille, joueur, ligne, colonne, type_jeu="4x4"):
    """Vérifie s'il y a 4 jetons du même joueur (numéro du joueur) alignés horizontalement à partir de la case d'une ligne et d'une colonne
    """

    # Changement du numéro de la colonne et de la ligne au rang
    ligne -= 1
    colonne -= 1

    # Extraction des cases à tester dans une liste si le type de jeu est en 4x4
    if type_jeu == "4x4":
        case_testees = [i for i in grille[ligne][colonne:colonne+4]]

    # Extraction des cases à tester dans une liste si le type de jeu est en 3x3
    elif type_jeu == "3x3":
        case_testees = [i for i in grille[ligne][colonne:colonne+3]]

    # Parcours de chaque élément à tester, dès qu'un est différent du numéro du joueur, alors renvoie faux, si aucun n'est différent, renvoie vrai.
    for case in case_testees:
        if case != joueur:
            return False
    return True

def vertical(grille, joueur, ligne, colonne, type_jeu="4x4"):
    """Vérifie s'il y a 4 jetons du même joueur (numéro du joueur) alignés verticalement à partir de la case d'une ligne et d'une colonne
    """

    # Changement du numéro de la colonne et de la ligne au rang
    ligne -= 1
    colonne -= 1

    # Extraction des cases à tester dans une liste si le type de jeu est en 4x4
    if type_jeu == "4x4":
        case_testees = [grille[i][colonne] for i in range(ligne, ligne+4)]
    
    # Extraction des cases à tester dans une liste si le type de jeu est en 3x3
    elif type_jeu == "3x3":
        case_testees = [grille[i][colonne] for i in range(ligne, ligne+3)]

    # Parcours de chaque élément à tester, dès qu'un est différent du numéro du joueur, alors renvoie faux, si aucun n'est différent, renvoie vrai.
    for case in case_testees:
        if case != joueur:
            return False
    return True

def diagonal(grille, joueur, ligne, colonne, type_jeu="4x4"):
    """Vérifie s'il y a 4 jetons du même joueur (numéro du joueur) alignés diagonalement dans toute les directions à partir de la case d'une ligne et d'une colonne
    """

    # Changement du numéro de la colonne et de la ligne au rang
    ligne -= 1
    colonne -= 1

    # Initialisation des variables de comptages et des paramètres en fonction du type du jeu
    ligne_reference, colonne_reference = ligne, colonne
    case_testees_haut_gauche = 0
    case_testees_haut_droite = 0
    case_testees_bas_gauche = 0
    case_testees_bas_droite = 0
    
    haut_possible = ligne >= 3 if type_jeu == "4x4" else ligne >= 2
    bas_possible = ligne <= 4 if type_jeu == "4x4" else ligne <= 5
    gauche_possible = colonne >= 3 if type_jeu == "4x4" else colonne >= 2
    droite_possible = colonne <= 6 if type_jeu == "4x4" else colonne <= 7
    boucle = range(4) if type_jeu == "4x4" else range(3)
    nombre_aligne_necessaire = 4 if type_jeu == "4x4" else 3

    # Test pour chaque directions s'il y à le bon nombre de pions alignés, renvoie vrai si c'est le cas
    if haut_possible and gauche_possible:        
        for i in boucle:
            case_testees_haut_gauche += 1 if grille[ligne][colonne] == joueur else 0
            colonne -= 1
            ligne -= 1
    
    if case_testees_haut_gauche == nombre_aligne_necessaire:
        return True
    ligne, colonne = ligne_reference, colonne_reference 

    if haut_possible and droite_possible:
        for i in boucle:
            case_testees_haut_droite += 1 if grille[ligne][colonne] == joueur else 0
            colonne += 1
            ligne -= 1

    if case_testees_haut_droite == nombre_aligne_necessaire:
        return True
    ligne, colonne = ligne_reference, colonne_reference 

    if bas_possible and gauche_possible:
        for i in boucle:
            case_testees_bas_gauche += 1 if grille[ligne][colonne] == joueur else 0
            colonne -= 1
            ligne += 1

    if case_testees_bas_gauche == nombre_aligne_necessaire:
        return True  
    ligne, colonne = ligne_reference, colonne_reference 

    if bas_possible and droite_possible:
        for i in boucle:
            case_testees_bas_droite += 1 if grille[ligne][colonne] == joueur else 0
            colonne += 1
            ligne += 1

    if case_testees_bas_droite == nombre_aligne_necessaire:
        return True

    # Si ce n'est pas le cas, renvoie faux
    return False

def victoire(grille, joueur, type_jeu="4x4"):
    """Renvoie vrai s'il y a sur la grille 4 jetons (numéro d'un même joueur) alignés de manière horizontale, verticale ou diagonale.
    """

    # Si le jeu est en 4x4
    if type_jeu == "4x4":
        # Vérification pour chaque case potentielle de manière horizontale 
        for ligne in range(1, 9):
            for colonne in range(1, 8):
                if horizontal(grille, joueur, ligne, colonne, type_jeu):
                    return True
        
        # Vérification pour chaque case potentielle de manière verticale
        for ligne in range(1, 6):
            for colonne in range(1, 11):
                if vertical(grille, joueur, ligne, colonne, type_jeu):
                    return True
        
        # Vérification pour chaque case potentielle de manière diagonale
        for ligne in range(1, 9):
            for colonne in range(1, 11):
                if diagonal(grille, joueur, ligne, colonne, type_jeu):
                    return True

        # Renvoie faux si aucune des situations n'a été détéctée
        return False 

    # Si le jeu est en 3x3
    else:
        # Vérification pour chaque case potentielle de manière horizontale 
        for ligne in range(1, 9):
            for colonne in range(1, 9):
                if horizontal(grille, joueur, ligne, colonne, type_jeu):
                    return True
        
        # Vérification pour chaque case potentielle de manière verticale
        for ligne in range(1, 7):
            for colonne in range(1, 11):
                if vertical(grille, joueur, ligne, colonne, type_jeu):
                    return True
        
        # Vérification pour chaque case potentielle de manière diagonale
        for ligne in range(1, 9):
            for colonne in range(1, 11):
                if diagonal(grille, joueur, ligne, colonne, type_jeu):
                    return True

        # Renvoie faux si aucune des situations n'a été détéctée
        return False           

def match_nul(grille):
    """Renvoie vrai si l'ensemble de la grille ne contient aucun 0, sinon, renvoie faux
    """

    # Parcours de chaque case de la grille puis test pour savoir si égal à 0
    for case in grille[0]:
        if case == 0:
            return False
    return True

def coup_aleatoire(grille, joueur):
    """Place le jeton du joueur (numéro du joueur) aléatoirement sur un emplcement disponible (case contenant 0) de la grille.
    """

    # Tant que le jeton n'est pas joué, on retente avec une valeur aléatoire
    while True:
        colonne = random.randint(1, 10)

        # Si le coup dans la colonne choisie aléatoirement est possible, alors on joue le jeton du joueur dans cette colonne
        if test_coup_possible(grille, colonne):
            jou(grille, joueur, colonne)
            return
        
        # S'il y a match nul, on arrete la boucle, permet d'éviter une boucle infinie en cas d'erreur
        if match_nul(grille): 
            return

#def coup_stratégique(grille, joueur):

def partie(nb_joueurs_humain, nb_joueurs_robots=0, vitesse=1):
    """Crée une partie de puissance 4. Le nombre de joueur total doit être de 2 ou 3, et le nombre de joueur robots ainsi qu'humain peut varier entre 1 et 3.
       La vitesse correspond on temps que mettent les robots à jouer afin d'éviter un programme trop rapide s'il n'y a que des robots, elle doit être comprise entre 0 et 1.
    """

    # Verifie que tout les paramètres soient corrects
    assert (3 >= nb_joueurs_humain >= 0 and type(nb_joueurs_humain) == int), "Le nombre de joueur doit être compris entre 1 et 3."
    assert (3 >= nb_joueurs_robots >= 0 and type(nb_joueurs_robots) == int), "Le nombre de robot doit être compris entre 1 et 3."
    assert (nb_joueurs_humain + nb_joueurs_robots < 4), "Il y a trop de joueur, le nombre maximal est 3."
    assert (nb_joueurs_humain + nb_joueurs_robots > 1), "Il n'y a pas assez de joueur, le nombre minimal est 2."
    assert (1 >= vitesse >= 0), "La vitesse doit être comprise entre 0 et 1."

    # Initialise les paramètres de la partie
    sec_pause = 1.1-vitesse
    grille = nouvelle_grille()
    nb_joueurs_total = nb_joueurs_humain + nb_joueurs_robots
    type_jeu = "4x4" if nb_joueurs_total == 2 else "3x3"
    print(type_jeu)
    # Determine tout les joueurs de la partie
    if nb_joueurs_total == nb_joueurs_robots:        
        if nb_joueurs_total == 3:
            lise_joueurs = ["robot_J1", "robot_J2", "robot_J3"]
        elif nb_joueurs_total == 2:
            lise_joueurs = ["robot_J1", "robot_J2"]

    elif nb_joueurs_total == nb_joueurs_humain:
        if nb_joueurs_total == 3:
            lise_joueurs = ["humain_J1", "humain_J2", "humain_J3"]
        elif nb_joueurs_total == 2:
            lise_joueurs = ["humain_J1", "humain_J2"]

    else:
        if nb_joueurs_humain == 1 and nb_joueurs_robots == 2:
            lise_joueurs = ["humain_J1", "robot_J2", "robot_J3"]
        elif nb_joueurs_humain == 2 and nb_joueurs_robots == 1:
            lise_joueurs = ["humain_J1", "humain_J2", "robot_J3"]
        else:
            lise_joueurs = ["humain_J1", "robot_J2"]
    
    # Debut de la partie       
    affiche(grille)       

    # A chaque tour, on récupère le numéro du joueur dont c'est le tour de jouer
    for tour in range(85):
        tour_joueur = tour % nb_joueurs_total

        # Si le joueur est un humain, alors on demande une valeur
        if lise_joueurs[tour_joueur][0:6] == "humain": 
            
            # Tant que le jeton n'est pas placé, on demande une valeur
            jeton_place = False
            while not jeton_place:

                # Entrée, vérification de la valeur et placement du jeton
                selection_case = input(f"Joueur J{lise_joueurs[tour_joueur][-1]}, choisis une colonne: ")
                try:
                    if 1 <= int(selection_case) <= 10:
                        if test_coup_possible(grille, int(selection_case)):
                            jou(grille, int(lise_joueurs[tour_joueur][-1]), int(selection_case))
                            jeton_place = True

                        else:
                            print("Vous ne pouvez pas placez de jeton ici, la colonne est pleine, réessayez.")
                    else:
                        print("Vous devez saisir un nombre entier compris entre 1 et 10, réessayez.")
                except:
                    print("Vous devez saisir un nombre entier compris entre 1 et 10, réessayez.")

        # Sinon, si le joueur est un robot, alors on génère une valeur aléatoire avec une courte pause pour permettre de suivre le jeu
        else: 
            coup_aleatoire(grille, int(lise_joueurs[tour_joueur][-1]))
            print(f"Le robot J{lise_joueurs[tour_joueur][-1]} réfléchit.")
            time.sleep(sec_pause+0.3)

        # On affichage la grille et on regarde s'il y a un gagnant
        affiche(grille)  

        if victoire(grille, int(lise_joueurs[tour_joueur][-1]), type_jeu):
            joueur = "joueur" if lise_joueurs[tour_joueur][0:6] == "humain" else "robot"
            print(f"Le {joueur} J{lise_joueurs[tour_joueur][-1]} a gagné !")
            return

        elif match_nul(grille):
            print("Il y a match nul.")
            return

partie(nb_joueurs_humain=1, nb_joueurs_robots=1, vitesse=0.1)