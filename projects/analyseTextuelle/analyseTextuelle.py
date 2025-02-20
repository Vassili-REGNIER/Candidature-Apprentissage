# Projet texte
# REGNIER_Vassili

"""
questions: 

 - fonction renverse
 - fonction occurence méthode 1
 - .lower à la fonction occurrence
 - fonction decompose caractères speciaux
"""

import doctest
import math
import string
import time

def renverse(chaine) :
    """Prend en argument une chaine de caractère, renvoie la chaine de caractère retournée.

    >>> renverse('bonjour')
    'ruojnob'
    >>> renverse('')
    ''
    """

    return chaine[::-1]

def test_palindrome(chaine) :
    """Prend en argument une chaine de caractère, renvoie vrai si cette chaine de caractère est un palindrome, renvoie faux dans le cas contraire.
    >>> test_palindrome("radar")
    True
    >>> test_palindrome("kaya")
    False
    >>> test_palindrome("laMarieeiraMal")
    True
    """
    # Un mot à une lettre n'est pas un palindrome
    if len(chaine) == 1:
        return False 

    chaine = chaine.lower()
    chaine_renversee = renverse(chaine)
    
    # Détermine la boucle en fonction de la parité de la taille de la chaine de caractère
    boucle = range(int(len(chaine) / 2)) if len(chaine) % 2 == 0 else range(math.floor(len(chaine) / 2))

    # Si on détecte au moins une différence avec 
    for i in boucle:
        if chaine[i] != chaine_renversee[i]:
            return False
    return True


def occurrence(chaine, lettre):
    """Renvoie un entier égal au nombre de fois qu'une lettre apparaît dans une chaine de caractères.

    >>> occurrence("bonjour","o")
    2
    >>> occurrence("Au revoir","z")
    0
    """

    # Méthode 1

    return chaine.count(lettre)

    # Méthode 2

    compteur = 0

    # Parcours des caractères de la chaine, si il est égale à la lettre, on ajoute 1 au compteur
    for caractere in chaine:
        if caractere == lettre:
            compteur += 1

    return compteur 


def idx_occurrence(chaine, lettre):
    """Prend en paramètre une chaine de caractères ainsi qu'une lettre, renvoie faux si la lettre n'est pas présente dans la chaine de caractères, sinon renvoie un tableau avec la liste des indices où la lettre est présente.
    
    >>> idx_occurrence("une chaine de caractère", "c")
    [4, 14, 18]
    """

    # Si la lettre n'apparais pas dans la chaine alors renvoie faux
    if occurrence(chaine, lettre) == 0:
        return False
    
    liste_indices = []

    # Parcours de le chaine de caractère, ajoute au tableau l'indice si la lettre est trouvée
    for indice in range(len(chaine)):
        if chaine[indice] == lettre:
            liste_indices.append(indice)

    return liste_indices

def occurrence_max(chaine) :
    """
    >>> occurrence_max("bonjour")
    ['o']
    >>> occurrence_max("val vale valet")
    ['a', 'l', 'v']
    """

    # Dictionnaire permettant de stocker l'occurence de chaque lettre dans la chaine de caractère
    occurrenceLettres = {}

    # Parcours chaque lettre de la chaine, si elle n'est pas dans le dictionnaire, on l'ajoute et lui donne la valeur 1, si elle est deja dans le dictionnaire, on incrémente la valeur de 1
    for indice in range(len(chaine)):    
        if chaine[indice] in occurrenceLettres:
            occurrenceLettres[chaine[indice]] += 1
        else:
            occurrenceLettres[chaine[indice]] = 1

    # Stocke la valeur de la plus grande occurrence d'une lettre et la ou les lettres la plus grande occurrence
    lettresOccurrenceMax = []
    indiceOccurrenceMax = 0

    # Parcours des lettres présentes dans la chaine
    for lettre in occurrenceLettres.keys():

        # Si son occurrence est plus grande que la plus grande occurrence, alors on écrase l'ancienne lettre/occurrence par les nouvelles valeurs
        if occurrenceLettres[lettre] > indiceOccurrenceMax:
            indiceOccurrenceMax = occurrenceLettres[lettre]
            lettresOccurrenceMax = [lettre]

        # Si son occurrence est égale, alors on ajoute la lettre au tableau
        elif occurrenceLettres[lettre] == indiceOccurrenceMax:
            lettresOccurrenceMax.append(lettre)
    
    lettresOccurrenceMax.sort()
    return lettresOccurrenceMax

def decompose(chaine) :
    """Prend en paramètre une chaine de caractère, retourne la liste des mots sans la ponctuation de cette chaine.

    >>> decompose("bonjour")
    ['bonjour']
    >>> decompose("Avez-vous vu l’hélicoptère ?")
    ['Avez', 'vous', 'vu', 'l', 'hélicoptère']
    """

    # Définit la ponctuation selon la bibliothèque string + ajout de l'espace et de "'’
    ponctuation = f'{string.punctuation} \"\'\’'
    mots = []
    mot = ""

    # Pour chaque caractère du mot
    for caractere in chaine:

        # Si il n'est pas une ponctuation on l'ajoute au mot
        if caractere not in ponctuation:
            mot += caractere

        # Sinon, cela signifie que la fin du mot est atteint, donc on l'ajoute à la liste de mot et on efface les caractères  
        else:
            if mot != "":
                mots.append(mot)
                mot = ""

    if mot != "":
        mots.append(mot)

    return mots

def recompose(tableau, separation=""):
    """Prend deux paramètres: un tableau de chaines de caractères et une chaine de caractère.
    Renvoie une chaine de caractère composé de toutes les chaines du tableau séparées par la seconde chaine de caractère.

    >>> recompose(["bonjour","à","tous","!"]," ")
    'bonjour à tous !'
    >>> recompose(["la","mariee","ira","mal"], "")
    'lamarieeiramal'
    >>> recompose(["cela","est","vraiment","pénible"], " -STOP- ")
    'cela -STOP- est -STOP- vraiment -STOP- pénible'
    """

    # Méthode 1

    return separation.join(tableau)

    # Methode 2

    # Ajout de la séparation à chaque chaine de tableau
    chaines_separees = [f'{tableau[i]}{separation}' for i in range(len(tableau))]
    
    # Assemblage de toutes les chaines du nouveau tableau avec les séparations
    chaine = "".join(chaines_separees)
    
    # Supression de la denière spération en trop
    chaine = chaine[:len(chaine)-len(separation)]

    return chaine

texte1 = "Un jour, Bob, un collectionneur de voitures anciennes décida de peindre sa voiture préférée en rouge. Cependant, lorsqu'il essaya de la sortir de son garage, il se rendit compte que l'espace était beaucoup trop étroit pour la faire sortir. Il était déçu, mais déterminé à trouver une solution. Finalement, il découvrit que s'il peignait la voiture en blanc, elle semblerait plus petite et pourrait sortir facilement."
texte2 = "Un jour de climat d'été, un musicien décida d'aller plonger dans les fonds marins pour trouver de nouvelles inspiration pour ses compositions. Après avoir laissé son kayak, lorsqu'il arriva au fond de l'océan, il vit une banane qui flottait tranquillement. Il la saisit et commença à en jouer comme s'il s'agissait d'une trompette. La banane produisait des sons incroyables, et le musicien put composer une mélodie unique grâce à elle."
texte3 = "Une fois, tôt dans la journée, une mandarine tomba du comptoir de la cuisine et roula sous le radiateur. Un enfant la vit et se mit à genoux pour la récupérer. Malheureusement, il se cogna la tête contre le radiateur et brisa un verre à côté de lui. Il pleura, mais son père arriva et lui expliqua que les accidents arrivent souvent et qu'il valait mieux ne pas pleurer pour un simple verre cassé."
texte4 = "Un jour, un amoureux de la nature décida de faire du vélo à travers les montagnes. Il monta sur son vélo et se mit en route, admirant les paysages magnifiques autour de lui. Après avoir rêver du paysage, il se rendit compte qu'il avait oublié son livre sur les rotors à la bibliothèque après avoir tater ses poches. Il décida alors de faire demi-tour pour aller le chercher, même s'il savait que cela signifiait une journée plus difficile à vélo. Arrivé, il se rend compte que le livre était dans sa poche, il dit 'J'aurais du retater ma veste'."
texte5 = "Un jour, un poisson nageait tranquillement dans un lac avec les autres poissons, lorsqu'il vit un avion voler très haut dans le ciel. Il était fasciné et décida de quitter son lac pour explorer le monde même si le chef des poissons l'avait interdit. Ce poissons détéstait le chef, il répétait souvent, ce chef à été elu par cette crapule. Il trouva un cactus et commença à grimper pour atteindre le ciel. Finalement, il arriva au sommet du cactus et put voir l'avion de ses propres yeux. Il était heureux d'avoir vécu cette aventure incroyable et décida de rentrer chez lui, nageant dans le lac avec un nouveau respect pour les merveilles du monde qui l'entouraient."

def analyse(texte, caractere=""):
    """
    """

    # Modification du texte pour analyser 
    texte_decompose = decompose(texte)
    texte_recompose = recompose(texte_decompose)

    # Analyse du texte

    # Test palindrome
    texteEstPalindrome = test_palindrome(texte_recompose)

    # Calcul nombre de mots/caractères/caractères sans espaces
    nbMots = len(texte_decompose)
    nbCaracteresTotal = len(texte)
    nbCaracteresSansEspaces = len(texte.replace(" ", ""))

    # Détermination du/des caractère le/les plus présent/présents, ainsi que le nombre de fois où il/ils apparait/apparaissent dans le texte
    caracterePlusPresent = occurrence_max(texte_recompose)
    nbCaracterePlusPresent = occurrence(texte_recompose, caracterePlusPresent[0])

    # Détermine les mots palindromes, ainsi que le nombre de mots palindromes 
    nbMotsPalindromes = 0
    motsPalindromes = []

    for mot in texte_decompose:
        if test_palindrome(mot):
            nbMotsPalindromes += 1
            motsPalindromes.append(mot)


    # Analyse du caractère choisis dans le texte si il a été définit
    if caractere != "":

        # Détermine le nombre de fois où le caractère apparait ainsi que l'indice de chaque apparition
        nbCaracteresX = occurrence(texte, caractere)
        idxCaracteresX = idx_occurrence(texte, caractere)

        # Détermine le mot/les mots avec le plus de fois ce caractère 
        motsMaxCaractereX = []
        nbCaracteresXDansMotMax = 0

        # Pour cela, on parcours tout les mots du texte en comptant le nombre de caractère X dans chaque mots 
        for mot in texte_decompose:
            nbCaracteresMot = occurrence(mot, caractere)

            # Si il est supérieur au précédent, alors il devient le nouveau mot avec le plus de fois le caratère X
            if nbCaracteresMot > nbCaracteresXDansMotMax:
                motsMaxCaractereX = [mot]

                # Et le nombre de caractères dans le mot max devient le nombre de caractère dans ce mot
                nbCaracteresXDansMotMax = nbCaracteresMot

            # Si il est égal, alors on l'ajoute à la liste des mots avec les plus de fois le caractère X
            elif nbCaracteresMot == nbCaracteresXDansMotMax:
                motsMaxCaractereX.append(mot)

        # Détermine le nombre de mots ayant le plus de fois le caractère x
        nbCaracteresMotMax = len(motsMaxCaractereX)

    # Sinon, on donne des valeurs aux variables pour pas provoquer d'erreurs
    else:
        nbCaracteresX = None
        idxCaracteresX = None
        nbCaracteresMotMax = None
        motsMaxCaractereX = None
        nbCaracteresXDansMotMax = None


    # Affectation de toutes les valeurs dans un dictionnaire
    analyse = {
        "texteEstPalindrome": texteEstPalindrome,
        "nbMots": nbMots,
        "nbCaracteresTotal": nbCaracteresTotal,
        "nbCaracteresSansEspaces": nbCaracteresSansEspaces,
        "nbMotsPalindromes": nbMotsPalindromes,
        "motsPalindromes": motsPalindromes,
        "caracterePlusPresent": caracterePlusPresent,
        "nbCaracterePlusPresent": nbCaracterePlusPresent,
        "caractereX": caractere,
        "nbCaracteresX": nbCaracteresX,
        "idxCaracteresX": idxCaracteresX,
        "nbCaracteresMotMax": nbCaracteresMotMax,
        "motsMaxCaractereX": motsMaxCaractereX,
        "nbCaracteresXDansMotMax": nbCaracteresXDansMotMax,
    }

    return analyse



def affichage(etape, analyse=None):
    """
    """
    
    if etape == "etape1":
        print(
            "╔═══════════════════════════════════════╗\n",
            "║     PROGRAMME D'ANALYSE TEXTUELLE     ║\n",
            "╠═══════════════════════════════════════╣\n",
            "║ Choissisez une texte:                 ║\n",
            "║                                       ║\n",
            "║   - [1] Choissisez un des 5 texte     ║\n",
            "║         préfabriqué                   ║\n",
            "║                                       ║\n",
            "║   - [2] Entrez votre propre texte     ║\n",
            "║                                       ║\n",
            "║                                       ║\n",
            "║              (Tapez stop pour sortir) ║\n",
            "╚═══════════════════════════════════════╝\n",
            sep="", end=""
        )

    elif etape == "etape1.1":
        print(
            "╔═══════════════════════════════════════╗\n",
            "║     PROGRAMME D'ANALYSE TEXTUELLE     ║\n",
            "╠═══════════════════════════════════════╣\n",
            "║ Ces textes ont été générés par beta   ║\n",
            "║ OpenAI à partir de trois mots clés    ║\n",
            "║ chacuns:                              ║\n",
            "║                                       ║\n",
            "║   - [1] Voiture, espace, peinture     ║\n",
            "║                                       ║\n",
            "║   - [2] Banane, plongée, trompette    ║\n",
            "║                                       ║\n",
            "║   - [3] Radiateur, verre, mandarine   ║\n",
            "║                                       ║\n",
            "║   - [4] Cyclisme, bibliothèque,       ║\n",
            "║         montagne                      ║\n",
            "║                                       ║\n",
            "║   - [5] Cactus, poisson, avion        ║\n",
            "║                                       ║\n",
            "║              (Tapez stop pour sortir) ║\n",
            "╚═══════════════════════════════════════╝\n",
            sep="", end=""
        )

    elif etape == "etape1.2":
        print(
            "╔═══════════════════════════════════════╗\n",
            "║     PROGRAMME D'ANALYSE TEXTUELLE     ║\n",
            "╠═══════════════════════════════════════╣\n",
            "║                                       ║\n",
            "║       Entrez votre propre texte       ║\n",
            "║                                       ║\n",
            "║                   V                   ║\n",
            "║                                       ║\n",
            "║              (Tapez stop pour sortir) ║\n",
            "╚═══════════════════════════════════════╝\n",
            sep="", end=""
        )

    elif etape == "etape2":
        for i in range(10):
          
            texte = "║            Analyse en cours           ║\n" if i != 9 else "║            Analyse terminée           ║\n"
            progression = f'║               {"▓"*(i)}{"░"*(9-i)}               ║\n'
            
            print(
                "╔═══════════════════════════════════════╗\n",
                "║     PROGRAMME D'ANALYSE TEXTUELLE     ║\n",
                "╠═══════════════════════════════════════╣\n",
                "║                                       ║\n",
                texte,
                "║                  ...                  ║\n",
                "║                                       ║\n",              
                progression,
                "║                                       ║\n",
                "╚═══════════════════════════════════════╝\n",
                sep="", end=""
            )
            time.sleep(0.3)

    elif etape == "etape3":

        # Création de toutes les phrases + mise en page

        phrase1 = f'║ Ce texte est un palindrome            ║\n' if analyse["texteEstPalindrome"] else f'║ Ce texte n\'est pas un palindrome      ║\n'
        phrase2 = f'║ - Nombre de mots: {str(analyse["nbMots"]) + " "*(5-len(str(analyse["nbMots"])))}               ║\n'
        phrase3 = f'║ - Nombre de caractères total: {str(analyse["nbCaracteresTotal"]) + " "*(5-len(str(analyse["nbCaracteresTotal"])))}   ║\n'
        phrase4 = f'║ - Nombre de caractères total hors     ║\n║ espaces: {str(analyse["nbCaracteresSansEspaces"]) + " "*(5-len(str(analyse["nbCaracteresSansEspaces"])))}                        ║\n'
        phrase5 = f'║ - Nombre de mots palindromes: {str(analyse["nbMotsPalindromes"]) + " "*(5-len(str(analyse["nbMotsPalindromes"])))}   ║\n'
        phrase6 = f'║ - Caractère le plus présent: {analyse["caracterePlusPresent"][0]}        ║\n' if len(analyse["caracterePlusPresent"]) == 1 else f'║ - Caractères les plus présents à      ║\n║ égalité: {", ".join(analyse["caracterePlusPresent"]) + " "*(29-len(", ".join(analyse["caracterePlusPresent"])))}║\n'
        phrase7 = f'║ - Nombre d\'apparition du caractère le ║\n║ plus présent: {str(analyse["nbCaracterePlusPresent"]) + " "*(24-len(str(analyse["nbCaracterePlusPresent"])))}║\n'

        # S'il n'y a aucun palindromes
        if analyse["nbMotsPalindromes"] != 0:
            listePalindromes = [f'║ * {palindrome + " "*(36-len(palindrome))}║\n' for palindrome in analyse["motsPalindromes"]]
            phrase8 = f'║   Liste des palindromes:              ║\n{"".join(listePalindromes)}'
        else:
            phrase8 = f'║   Liste des palindromes:              ║\n║    Aucun                              ║\n'


        # Si la lettre à été définie alors on crée les phrase d'affichage
        if analyse["caractereX"] != "":

            # Si elle a été repérée au moins une fois, on poursuit
            if analyse["idxCaracteresX"] != 0:
                phrase9 =  f'║   Informations sur la lettre {analyse["caractereX"]}:       ║\n'
                phrase10 = f'║ - Nombre d\'apparitions: {str(analyse["nbCaracteresX"]) + " "*(14-len(str(analyse["nbCaracteresX"])))}║\n'

            
                if len(analyse["idxCaracteresX"]) % 2 == 0:
                    listePositions = [f'║     #{str(analyse["idxCaracteresX"][i] + 1) + " "*(10-len(str(analyse["idxCaracteresX"][i] + 1)))}         #{str(analyse["idxCaracteresX"][i+1] + 1) + " "*(10-len(str(analyse["idxCaracteresX"][i+1] + 1)))}   ║\n' for i in range(0, len(analyse["idxCaracteresX"]), 2)]
                else:
                    listePositions = [f'║     #{str(analyse["idxCaracteresX"][i] + 1) + " "*(10-len(str(analyse["idxCaracteresX"][i] + 1)))}         #{str(analyse["idxCaracteresX"][i+1] + 1) + " "*(10-len(str(analyse["idxCaracteresX"][i+1] + 1)))}   ║\n' for i in range(0, len(analyse["idxCaracteresX"])-1, 2)] 
                    listePositions.append(f'║     #{str(analyse["idxCaracteresX"][-1] + 1) + " "*(10-len(str(analyse["idxCaracteresX"][-1] + 1)))}                       ║\n')
                
                phrase11 = f'║ - Liste des positions de la lettres:  ║\n{"".join(listePositions)}║                                       ║\n'

                listeMots = [f'║    *{mot}{" "*(34-len(mot))}║\n' for mot in analyse["motsMaxCaractereX"]]
                phrase12 = f'║ Le mot:                               ║\n{"".join(listeMots)}' if analyse["nbCaracteresMotMax"] == 1 else  f'║ Les {analyse["nbCaracteresMotMax"]} mots:{" "*(28-len(str(analyse["nbCaracteresMotMax"])))}║\n{"".join(listeMots)}'
                phrase13 = f'║ possède {analyse["nbCaracteresXDansMotMax"]} fois la lettre {analyse["caractereX"]}            ║\n' if analyse["nbCaracteresMotMax"] == 1 else f'║ possèdent {analyse["nbCaracteresXDansMotMax"]} fois la lettre {analyse["caractereX"]}          ║\n'

                phrasesLettreX = phrase9 + phrase10 + phrase11 + phrase12 + phrase13

            # Sinon, le programme affiche que la lettre n'a pas été trouvée dans le texte
            else:
                phrasesLettreX = f'║ La lettre {analyse["caractereX"]} n\'as pas été trouvée dans ║\n║ le texte                              ║\n'

        # Sinon, on donne un chaine vide comme valeur pour pas provoquer d'erreur lors de l'affichage
        else:
            phrasesLettreX = ""

        print(
            "╔═══════════════════════════════════════╗\n",
            "║     PROGRAMME D'ANALYSE TEXTUELLE     ║\n",
            "╠═══════════════════════════════════════╣\n",
            phrase1,
            "║            ╔══════════════╗           ║\n",
            "║            ║ Statistiques ║           ║\n",
            "║            ╚══════════════╝           ║\n",
            phrase2,
            phrase3,
            phrase4,
            phrase5,
            phrase6,
            phrase7,
            "║                                       ║\n",
            phrase8,
            "║                                       ║\n",
            phrasesLettreX,
            "║                                       ║\n",
            "║                                       ║\n",
            "║   Tapez:  - stop, pour sortir         ║\n",
            "║           - suivant, pour recommencer ║\n",
            "╚═══════════════════════════════════════╝\n",
            sep="", end=""
        )

def choixLettre():
    while True:
        lettre = input("    Choissisez une lettre à analyser, pour ignorer, tapez 'non'.\n  >>> ")
        if lettre in string.ascii_letters and len(lettre) == 1:
            return lettre
        elif lettre.lower() == "non":
            return ""

def analyse_textuelle():

    en_cours = True
    while en_cours:

        etape = "etape1"
        texte = ""

        affichage(etape)
        while etape == "etape1":
            
            entree = input("  >>> ")

            if entree.lower() == "stop":
                return

            elif entree == "1":
                etape = "etape1.1"
            
            elif entree == "2":
                etape = "etape1.2"

            else:
                print("    Tapez 1 ou 2.")

        affichage(etape)

        while etape == "etape1.1":
            

            entree = input("  >>> ")

            if entree.lower() == "stop":
                return

            elif entree == "1":
                texte = texte1
                lettre = choixLettre()
                etape = "etape2"

            elif entree == "2":
                texte = texte2
                lettre = choixLettre()
                etape = "etape2"

            elif entree == "3":
                texte = texte3
                lettre = choixLettre()
                etape = "etape2"

            elif entree == "4":
                texte = texte4
                lettre = choixLettre()
                etape = "etape2"

            elif entree == "5":
                texte = texte5
                lettre = choixLettre()
                etape = "etape2"

            else:
                print("    Tapez 1, 2, 3, 4 ou 5.")

        while etape == "etape1.2":

            while texte == "":
                texte = input("  >>> ")

            if entree.lower() == "stop":
                return

            entree = ""
            while entree != "VALIDER":
                entree = input("    C'est enregistré, pour valider, tapez 'VALIDER', ou retapez votre texte.\n  >>> ")
                if entree == "VALIDER":
                    lettre = choixLettre()
                    etape = "etape2"
                else:
                    texte = entree

        affichage(etape)
        etape = "etape3"
        affichage(etape, analyse(texte, lettre))

        fin = True
        while fin:
            entree = input("  >>> ")

            if entree.lower() == "stop":
                return
            
            if entree.lower() == "suivant":
                fin = False


analyse_textuelle()
    


"""
    analyse = {
        "texteEstPalindrome": texteEstPalindrome, aaaaaa
        "nbMots": nbMots, aaaaaa
        "nbCaracteresTotal": nbCaracteresTotal, aaaaa
        "nbCaracteresSansEspaces": nbCaracteresSansEspaces, aaaaa
        "nbMotsPalindromes": nbMotsPalindromes, aaaaaa
        "motsPalindromes": motsPalindromes, aaa
        "caracterePlusPresent": caracterePlusPresent, aaaaa
        "nbCaracterePlusPresent": nbCaracterePlusPresent, aaaa
        "caractereX": caractere, aaaaa
        "nbCaracteresX": nbCaracteresX, aaaaaaa
        "idxCaracteresX": idxCaracteresX, aaaaaa
        "nbCaracteresMotMax": nbCaracteresMotMax, aa 
        "motsMaxCaractereX": motsMaxCaractereX, aaaa 
        "nbCaracteresXDansMotMax": nbCaracteresXDansMotMax, aa
    }"""

print(doctest.testmod())

