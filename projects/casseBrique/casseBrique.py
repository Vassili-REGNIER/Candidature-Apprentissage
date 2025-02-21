# REGNIER Vassili & MARTIN-ROSSET Clara

import random  # Importation du module random
import sys  # Importation du module sys
import pygame  # Importation du module pygame
import pygame.freetype  # Importation du module pygame.freetype
import math  # Importation du module math
pygame.init()  # Initialisation du module pygame
pygame.freetype.init()  # Initialisation du module pygame.freetype
font_1 = pygame.freetype.SysFont(None, 15)  # Création d'une police avec une taille de 15 pixels
font_2 = pygame.freetype.SysFont(None, 25)
largeur, hauteur = 790, 480
jeu_en_cours = False  # Gère la phase du jeu
retire_vie = False  # Gère la suppression de vie

# Création des fonds d'écrans
background_start_menu = pygame.image.load('bg_start_menu.png')
background_start_menu = pygame.transform.scale(background_start_menu, (largeur, hauteur))
background_game_over = pygame.image.load('bg_game_over.png')
background_game_over = pygame.transform.scale(background_game_over, (largeur, hauteur))
bg_niveau_3vies = pygame.image.load('bg_niveau_3vies.png')
bg_niveau_3vies = pygame.transform.scale(bg_niveau_3vies, (largeur, hauteur))
bg_niveau_2vies = pygame.image.load('bg_niveau_2vies.png')
bg_niveau_2vies = pygame.transform.scale(bg_niveau_2vies, (largeur, hauteur))
bg_niveau_1vie = pygame.image.load('bg_niveau_1vie.png')
bg_niveau_1vie = pygame.transform.scale(bg_niveau_1vie, (largeur, hauteur))

background = background_start_menu  # Variable globale permettant de choisir le fond d'écran actuel
screen = pygame.display.set_mode((largeur, hauteur))  # Création de la fenêtre de jeu
pygame.display.set_caption("Casse-Brique")  # Définition du titre de la fenêtre de jeu
clock = pygame.time.Clock()  # Création d'une instance pour gérer le temps du jeu
white = (255, 255, 255)  # Définition de la couleur blanche
black = (0, 0, 0)  # Définition de la couleur noire
red = (255, 0, 0)  # Définition de la couleur rouge

# Définit les différentes couleurs des briques
couleurs_briques = [
    (255, 255, 255),  # Blanc
    (0, 255, 0),      # Vert
    (255, 255, 0),    # Jaune
    (255, 165, 0),    # Orange
    (255, 0, 0),      # Rouge
    (255, 192, 203),  # Rose
    (0, 0, 0)         # Noir
]

x_min, y_min = 0, 0  # Définition des coordonnées minimales de la fenêtre
x_max, y_max = largeur, hauteur  # Définition des coordonnées maximales de la fenêtre
niveau_slectionne = 1  # Enregistre le niveau actuellement séléctionné

# Crée les différents niveaux
niveaux = {
    'num niveau':['arriere plan', 'rayon_balle', 'longueur raquette', 'vitesse balle'],
    1:['bg1', 10, 10, 8],
    2:['bg1', 9, 7, 10],
    3:['bg1', 8, 5, 12],
}

class Balle:
    def vitesse_par_angle(self, angle):
        self.vx = self.vitesse * math.cos(math.radians(angle))  # Calcul de la composante x de la vitesse
        self.vy = -self.vitesse * math.sin(math.radians(angle))  # Calcul de la composante y de la vitesse

    def __init__(self):
        global niveau_slectionne
        self.x, self.y = (400, 400)  # Modification de la position initiale de la balle
        self.vitesse = niveaux[niveau_slectionne][3] # vitesse initiale en fonction du niveau
        self.dx = random.randint(-5, 5)  # Direction horizontale aléatoire (-5 ou 5)
        self.dy = -5  # Direction verticale constante
        self.sur_raquette = True  # Ajout d'un attribut pour indiquer si la balle est sur la raquette ou non

    def afficher(self):
        rayon_balle = niveaux[1][1]
        pygame.draw.circle(screen, white, (int(self.x), int(self.y)), rayon_balle)  # Affichage de la balle

    def rebond_raquette(self, raquette):  # Def méthode pour gérer le rebond de la balle sur la raquette
        rayon_balle = niveaux[1][1]
        diff = raquette.x - self.x
        longueur_totale = raquette.longueur / 2 + rayon_balle  # Calcul  longueur totale pour le rebond
        angle = 90 + 80 * diff / longueur_totale  # Calcul angle de rebond
        self.vitesse_par_angle(angle)  # Calcul vecteur vitesse après le rebond

    def deplacer(self, raquette):  # Def méthode pour déplacer la balle
        rayon_balle = niveaux[1][1]
        if self.sur_raquette:  # Vérifie si la balle est sur la raquette
            self.y = raquette.y - 2 * rayon_balle  # Modifie la position de la balle en fonction de la raquette
            self.x = raquette.x  # Modifie la position de la balle en fonction de la raquette
        else:
            self.x += self.vx  # Déplace la balle selon sa vitesse horizontale
            self.y += self.vy  # Déplace la balle selon sa vitesse verticale
            if raquette.collision_balle(self) and self.vy > 0:  # Vérifie s'il y a une collision entre la raquette et la balle
                self.rebond_raquette(raquette)  # Applique le rebond sur la raquette
            if self.x + rayon_balle > x_max:  # Vérifie si la balle dépasse le côté droit de l'écran
                self.vx = -self.vx  # Inverse la direction de la balle selon l'axe des x
            if self.x - rayon_balle < x_min:  # Vérifie si la balle dépasse le côté gauche de l'écran
                self.vx = -self.vx  # Inverse la direction de la balle selon l'axe des x
            if self.y + rayon_balle > y_max:  # Vérifie si la balle dépasse le bas de l'écran
                self.sur_raquette = True  # Indique que la balle est à nouveau sur la raquette
                global retire_vie
                retire_vie = True
            if self.y - rayon_balle < y_min:  # Vérifie si la balle dépasse le haut de l'écran
                self.vy = -self.vy  # Inverse la direction de la balle selon l'axe des y

class Raquette:
    def __init__(self):
        global niveau_slectionne
        self.x = (x_min + x_max) / 2  # Position initiale de la raquette
        self.y = y_max - (3 + niveaux[niveau_slectionne][1])  # Position verticale de la raquette
        self.longueur = 25 * niveaux[niveau_slectionne][2]  # Longueur de la raquette

    def collision_balle(self, balle):  # Def méthode pour gérer la collision entre la balle et la raquette
        rayon_balle = niveaux[1][1]
        vertical = abs(self.y - balle.y) < 2 * rayon_balle  # Vérifie s'il y a une collision verticale
        horizontal = abs(self.x - balle.x) < self.longueur / 2 + rayon_balle  # Vérifie s'il y a une collision horizontale
        return vertical and horizontal  # Retourne TRUE si les deux types de collisions sont vérifiés

    def afficher(self):  # Def méthode pour afficher la raquette
        rayon_balle = niveaux[1][1]
        pygame.draw.rect(screen, white, (int(self.x - self.longueur / 2), int(self.y - rayon_balle), self.longueur, 2 * rayon_balle), 0)  # Affichage de la raquette

    def deplacer(self, x):  # Def méthode pour déplacer la raquette en fonction de la position de la souris
        if x - self.longueur / 2 < x_min:  # Vérifie si la raquette dépasse le côté gauche de l'écran
            self.x = x_min + self.longueur / 2  # Place la raquette au bord gauche de l'écran
        elif x + self.longueur / 2 > x_max:  # Vérifie si la raquette dépasse le côté droit de l'écran
            self.x = x_max - self.longueur / 2  # Place la raquette au bord droit de l'écran
        else:
            self.x = x  # Place la raquette à la position de la souris

class Jeu:
    def __init__(self, niveau):
        self.niveau = niveau
        self.balle = Balle()
        self.raquette = Raquette()
        self.generation_brique()
        self.vies_restantes = 3

    def generation_brique(self):
        """ Initialise l'atribut briques de l'instance jeu en fonction du niveau sélectionné 
        """
        briques = []
        for ligne in range(3 + int(self.niveau)):
            for colonne in range(14):
                x = colonne * (50 + 5) + 40
                y = ligne * (34 + 1) + 20
                vies = random.randint(int(self.niveau), int(self.niveau)*2)  # Nombre de vies aléatoire (entre 1 et le numéro du niveau)
                brique = Brique(x, y, vies)
                briques.append(brique)
        self.briques = briques

    def actualise_etat(self):
        global background
        global retire_vie

        # Retire une vie si la balla a dépassé la raquette
        if retire_vie:
            self.vies_restantes -= 1
            retire_vie = False

        # Modifie l'arrière plan en fonction du nombre de vies restantes
        if self.vies_restantes >= 3:
            background = bg_niveau_3vies
        elif self.vies_restantes == 2:
            background = bg_niveau_2vies
        elif self.vies_restantes == 1:
            background = bg_niveau_1vie
        else:
            background = background_game_over
            global jeu_en_cours
            jeu_en_cours = False
            self.fin_du_jeu()

    def fin_du_jeu(self):
        global background
        fin_jeu_en_cours = True
        while fin_jeu_en_cours:
            for event in pygame.event.get():  # Récupère les événements du jeu
                if event.type == pygame.QUIT:  # Vérifie s'il y a un événement de fermeture de la fenêtre
                    sys.exit()  # Ferme le jeu
                elif event.type == pygame.MOUSEBUTTONDOWN:   # Vérifie s'il y a un événement de clic de souris
                    if event.button == 1:  # Vérifie s'il s'agit du bouton gauche de la souris
                        background = background_start_menu
                        fin_jeu_en_cours = False
            screen.blit(background, (0, 0))  # Afficher le fond d'ecran 
            pygame.display.flip()   # Mettre à jour l'affichage


    def mise_a_jour(self):  # Met à jour le jeu

        self.actualise_etat()
        x, y = pygame.mouse.get_pos()  # Récupère la position de la souris
        self.balle.deplacer(self.raquette)  # Déplace la balle en fonction de la raquette
        self.raquette.deplacer(x)  #  Déplace la raquette en fonction de la position x de la souris
        for brique in self.briques:  # Pour chacune des briques
            if brique.en_vie():  # Si la brique est toujours en vie
                brique.collision_balle(self.balle)  # Gère la collision entre la brique et la balle
                self.raquette.deplacer(x)  # Déplace la raquette en fonction de la position de la souris

    def affichage(self):   # Affiche les éléments du jeu
        # Afficher le fond d'ecran 
        global background
        screen.blit(background, (0, 0))
        self.balle.afficher()  # Affiche la balle
        self.raquette.afficher()  # Affiche la raquette
        for brique in self.briques:  # Pour chacunes des briques
            if brique.en_vie():  # Si la brique est encore en vie
                brique.afficher()  # Affichage de la brique
            if self.balle.sur_raquette:
                draw_text("Cliquez pour commencer", font_2, white, screen, largeur // 2 - 150, hauteur // 2)

    def gestion_evenements(self):  # Gère les événements du jeu
        for event in pygame.event.get():  # Récupère les événements du jeu
            if event.type == pygame.QUIT:  # Vérifie s'il y a un événement de fermeture de la fenêtre
                sys.exit()  # Ferme le jeu
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Vérifie s'il y a un événement de clic de souris
                if event.button == 1:  # Vérifie s'il s'agit du bouton gauche de la souris
                    if self.balle.sur_raquette:  # Vérifie si la balle est sur la raquette
                        self.balle.sur_raquette = False  # Indique que la balle n'est plus sur la raquette
                        self.balle.vitesse_par_angle(60)  # Définit l'angle de départ de la balle après le clic

class Brique:
    def __init__(self, x, y, vie=1):
        rayon_balle = niveaux[1][1]  # Définit le rayon de la balle en fonction du niveau
        self.x = x  # Initialise la coordonnée x de la brique
        self.y = y  # Initialise la coordonnée y de la brique
        self.vie = vie  # Initialise la vie de la brique à 1
        self.longueur = 5 * rayon_balle  # Calcule la longueur de la brique en fonction du rayon de la balle
        self.largeur = 3 * rayon_balle  # Calcule la largeur de la brique en fonction du rayon de la balle

    def en_vie(self):
        return self.vie > 0  # Renvoie vrai si la vie de la brique est supérieure à 0

    def afficher(self):
        pygame.draw.rect(screen, couleurs_briques[self.vie - 1], (int(self.x - self.longueur/2),
                                         int(self.y - self.largeur/2), self.longueur, self.largeur), 0)  # Affiche la brique en modifiant sa couleur en fonction de sa vie

    def collision_balle(self, balle):
        rayon_balle = niveaux[1][1]  # Définit le rayon de la balle en fonction du niveau
        # on suppose que largeur<longueur
        marge = self.largeur/2 + rayon_balle
        dy = balle.y - self.y   # Calcul de la différence en y de la balle et la brique
        touche = False  # Par défaut, affecte False à la variable touche
        if balle.x >= self.x:  # On regarde à droite
            dx = balle.x - (self.x + self.longueur/2 - self.largeur/2)  # Calcul de la différence en x entre la position de la balle et le coté droit de la brique
            if abs(dy) <= marge and dx <= marge:  # Si la balle touche la brique
                touche = True  # Affecte True à la variable touche
                if dx <= abs(dy):  # Vérifie si la différence en x entre la balle et la brique est inférieure ou égale à la valeur absolue de la différence en y
                    balle.vy = -balle.vy  # Inverse la direction de la balle selon l'axe des y
                else:  # a droite
                    balle.vx = -balle.vx  # Inverse la direction de la balle selon l'axe des x
        else:  # on regarde a gauche
            dx = balle.x - (self.x - self.longueur/2 + self.largeur/2)  # Calcul de la différence en x entre la position de la balle et le coté gauche de la brique
            if abs(dy) <= marge and -dx <= marge:  # Si la balle touche la brique
                touche = True  # Affecte True à la variable touche
                if -dx <= abs(dy):  # Vérifie si l'opposé de la différence en x entre la balle et la brique est inférieure ou égale à la valeur absolue de la différence en y
                    balle.vy = -balle.vy  # Inverse la direction de la balle selon l'axe des y
                else:  # a gauche
                    balle.vx = -balle.vx  # Inverse la direction de la balle selon l'axe des x
        if touche:  # Si il y a une collision
            self.vie -= 1  # Réduit le nombre de vie de la brique 
        return touche  # Renvoie True s'il y a eu une collision et False sinon

# Fonction pour afficher le texte
def draw_text(text, font, color, surface, x, y):
    text_surface, rect = font.render(text, color)  # Définit la zone de texte
    surface.blit(text_surface, (x, y))  # Affiche le texte à la position x, y

def modifie_niveau(niveau):
    global niveau_slectionne
    niveau_slectionne = niveau

# Fonction pour créer un bouton
def draw_button(x, y, width, height, color, text, text_color, action=None, *args):
    global niveau_slectionne
    if text[-1].isdigit() and niveau_slectionne == int(text[-1]) and text.startswith("Niveau "):
        color = red

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            action(*args)

    else:
        pygame.draw.rect(screen, color, (x, y, width, height))

    draw_text(text, font_1, white, screen, x + 10, y + 10)

# Fonction pour démarrer le jeu
def start_game():
    global niveau_slectionne
    jeu = Jeu(niveau_slectionne)
    global jeu_en_cours
    jeu_en_cours = True
    while jeu_en_cours:  # Boucle principale du jeu
        jeu.gestion_evenements()
        jeu.mise_a_jour()
        jeu.affichage()
        pygame.display.flip()  # Rafraîchit l'affichage
        clock.tick(60)  # Attends pour ne pas dépasser 60 images/seconde

# Boucle principale du menu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Afficher le fond d'ecran du menu
    screen.blit(background, (0, 0))

    # Afficher les boutons
    draw_button(largeur // 2 - 50, hauteur // 2, 100, 50, black, "Start", white, start_game)
    draw_button(largeur // 2 - 50 - 125, hauteur // 2 + 100, 100, 50, black, "Niveau 1", white, modifie_niveau, 1)
    draw_button(largeur // 2 - 50, hauteur // 2 + 100, 100, 50, black, "Niveau 2", white, modifie_niveau, 2)
    draw_button(largeur // 2 - 50 + 125, hauteur // 2 + 100, 100, 50, black, "Niveau 3", white, modifie_niveau, 3)

    # Mettre à jour l'affichage
    pygame.display.flip()
