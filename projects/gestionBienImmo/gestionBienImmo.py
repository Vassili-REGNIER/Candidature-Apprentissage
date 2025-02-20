""" Projet réalisé par MARTIN-ROSSET Clara et REGNIER Vassili

    Clara s'est occupé de: la classe ABR et la majorité des méthodes, la classe Application, la fonction importer_fichier_csv() et la fonction afficher_erreur()

    Vassili s'est occupé de: la classe Bien_immo ainsi que toutes ses méthodes, les méthodes suppression() et insertion(), la classe ABR et la classe Application()
"""

import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog as sd
import csv

class Bien_immo:
    """
    Represents a real estate property.

    Attributes:
        nom (str): The name of the real estate property.
        nature (str): The nature of the real estate property (e.g., house, apartment).
        surface (float): The surface area of the real estate property in square meters.
        prix_moyen (float): The average price per square meter of the real estate property.
    
    Methods:
        estimation(): Calculates the estimated value of the real estate property based on its nature.
    """

    def __init__(self, nom, nature, surface, prix_moyen):
        """
        Initialize a new instance of the Bien_immo class.

        Args:
            nom (str): The name of the real estate property.
            nature (str): The nature of the real estate property (e.g., House, Apartment, Land).
            surface (float): The surface area of the real estate property in square meters.
            prix_moyen (float): The average price per square meter of the real estate property in euros.
        """
        self.nom = nom
        self.nat = nature
        self.surf = surface
        self.pmoy = prix_moyen

    def estimation(self):
        """
        Calculate the estimated value of the real estate property based on its nature, surface, and average price per square meter.

        Returns:
            float: The estimated value of the real estate property.
        """
        # Calcul de l'estimation en fonction de la nature du bien
        estimation_base = self.surf * self.pmoy

        # Tenir compte de la nature du bien
        if self.nat.lower() == "maison":
            # Augmenter l'estimation de 10% pour les maisons
            estimation_base *= 1.1
        elif self.nat.lower() == "entrepot":
            # Diminuer l'estimation de 20% pour les entrepôts
            estimation_base *= 0.8

        return estimation_base
    
class ABR:
    """
    Represents a binary search tree (Arbre Binaire de Recherche).

    Attributes:
        root (Node): The root node of the binary search tree.

    Methods:
        insertion(bien_immo, critere_tri): Inserts a new real estate property into the binary search tree.
        suppression(bien_immo, critere_tri): Removes a real estate property from the binary search tree.
        parcours_infixe(): Performs an inorder traversal of the binary search tree.
    """

    def __init__(self, racine):
        """
        Initialize a new instance of the ABR class.

        Args:
            racine: The root node of the binary search tree.
        """
        self.racine = racine
        self.gauche = None
        self.droit = None

    def test_vide(self):
        """
        Check if the binary search tree is empty.

        Returns:
            bool: True if the binary search tree is empty, False otherwise.
        """
        return self.gauche is None or self.droit is None

    def get_val(self):
        """
        Get the value of the current node.

        Returns:
            object: The value of the current node.
        """
        if self.racine:
            return self.racine.bien
        return None

    def get_gauche(self):
        """
        Get the left child node.

        Returns:
            object: The left child node.
        """
        if self.gauche:
            return self.racine.gauche
        return None

    def get_droit(self): 
        """
        Get the right child node.

        Returns:
            object: The right child node.
        """
        if self.racine:
            return self.racine.droit
        return None
    
    def insert_gauche(self, valeur):
        """
        Insert a new node as the left child.

        Args:
            valeur: The value to be inserted as the left child node.
        """
        if self.gauche == None:
            self.gauche = ABR(valeur)

    def insert_droit(self, valeur):
        """
        Insert a new node as the right child.

        Args:
            valeur: The value to be inserted as the right child node.
        """
        if self.droit == None:
            self.droit = ABR(valeur)
    
    def parcours_infixe(self):
        """
        Perform an inorder traversal of the binary search tree.

        Returns:
            list: A list of elements obtained from the inorder traversal.
        """
        elements = []
        if self.gauche:
            elements.extend(self.gauche.parcours_infixe())
        elements.append(self.racine)
        if self.droit:
            elements.extend(self.droit.parcours_infixe())
        return elements

    def insertion(self, bien_immo, critere_tri=1):
        """
        Insert a new property into the binary search tree based on the specified criteria.

        Args:
            bien_immo: The property to be inserted.
            critere_tri (int): The criteria for insertion (1: name, 2: nature, 3: surface, 4: average price).
        """
        if not bien_immo: return 
        
        if self.racine == None:
            self.racine = bien_immo

        elif critere_tri == 1:  # Il faut insérer par rapport au nom du bien
            if self.racine.nom > bien_immo.nom:  # Il faut insérer à gauche
                if self.gauche == None:
                    self.insert_gauche(bien_immo)
                else:
                    self.gauche.insertion(bien_immo, 1)
            else:  # Il faut insérer à droite
                if self.droit == None:
                    self.insert_droit(bien_immo)
                else:
                    self.droit.insertion(bien_immo, 1)
        
        elif critere_tri == 2:  # Il faut insérer par rapport à la nature du bien
            if self.racine.nat > bien_immo.nat:  # Il faut insérer à gauche
                if self.gauche == None:
                    self.insert_gauche(bien_immo)
                else:
                    self.gauche.insertion(bien_immo, 2)
            else:  # Il faut insérer à droite
                if self.droit == None:
                    self.insert_droit(bien_immo)
                else:
                    self.droit.insertion(bien_immo, 2)

        elif critere_tri == 3:  # Il faut insérer par rapport à la surface du bien
            if self.racine.surf > bien_immo.surf:  # Il faut insérer à gauche
                if self.gauche == None:
                    self.insert_gauche(bien_immo)
                else:
                    self.gauche.insertion(bien_immo, 3)
            else:  # Il faut insérer à droite
                if self.droit == None:
                    self.insert_droit(bien_immo)
                else:
                    self.droit.insertion(bien_immo, 3)
        
        elif critere_tri == 4:  # Il faut insérer par rapport au prix moyen du bien
            if self.racine.pmoy > bien_immo.pmoy:  # Il faut insérer à gauche
                if self.gauche == None:
                    self.insert_gauche(bien_immo)
                else:
                    self.gauche.insertion(bien_immo, 4)
            else:  # Il faut insérer à droite
                if self.droit == None:
                    self.insert_droit(bien_immo)
                else:
                    self.droit.insertion(bien_immo, 4)

    def suppression(self, bien_immo, critere_tri):
        """
        Remove a property from the binary search tree based on the specified criteria.

        Args:
            bien_immo: The property to be removed.
            critere_tri (int): The criteria for removal (1: name, 2: nature, 3: surface, 4: average price).
        """
        if self.racine is None:
            return self

        elif critere_tri == 1:
            # Si le bien à supprimer est plus petit que la racine, il est à gauche
            if bien_immo.nom < self.racine.nom:
                self.gauche = self.gauche.suppression(bien_immo, critere_tri)

            # Si le bien à supprimer est plus grand que la racine, il est à droite
            elif bien_immo.nom > self.racine.nom:
                self.droit = self.droit.suppression(bien_immo, critere_tri)

            # Si le bien n'est pas le bon, de part la manière dont fonctionne la classe ABR, le bien sera alors à droite
            elif not (bien_immo.nom == self.racine.nom and bien_immo.nat == self.racine.nat and bien_immo.surf == self.racine.surf and bien_immo.pmoy == self.racine.pmoy):
                self.droit = self.droit.suppression(bien_immo, critere_tri)
            
            # Si le bien à supprimer est égal à la racine
            else:
                # Cas 1 : Pas d'enfant gauche
                if self.gauche is None:
                    temp = self.droit
                    self = None
                    return temp

                # Cas 2 : Pas d'enfant droit
                elif self.droit is None:
                    temp = self.gauche
                    self = None
                    return temp

                # Cas 3 : Le bien à supprimer a deux enfants
                temp = self.valeur_noeud_minimum(self.droit)
                self.racine = temp.racine
                self.droit = self.droit.suppression(temp.racine, critere_tri)
            
            return self
        
        elif critere_tri == 2:
            # Si le bien à supprimer est plus petit que la racine, il est à gauche
            if bien_immo.nat < self.racine.nat:
                self.gauche = self.gauche.suppression(bien_immo, critere_tri)

            # Si le bien à supprimer est plus grand que la racine, il est à droite
            elif bien_immo.nat > self.racine.nat:
                self.droit = self.droit.suppression(bien_immo, critere_tri)

            # Si le bien n'est pas le bon, de part la manière dont fonctionne la classe ABR, le bien sera alors à droite
            elif not (bien_immo.nom == self.racine.nom and bien_immo.nat == self.racine.nat and bien_immo.surf == self.racine.surf and bien_immo.pmoy == self.racine.pmoy):
                self.droit = self.droit.suppression(bien_immo, critere_tri)
            
            # Si le bien à supprimer est égal à la racine
            else:
                # Cas 1 : Pas d'enfant gauche
                if self.gauche is None:
                    temp = self.droit
                    self = None
                    return temp

                # Cas 2 : Pas d'enfant droit
                elif self.droit is None:
                    temp = self.gauche
                    self = None
                    return temp

                # Cas 3 : Le bien à supprimer a deux enfants
                temp = self.valeur_noeud_minimum(self.droit)
                self.racine = temp.racine
                self.droit = self.droit.suppression(temp.racine, critere_tri)
            
            return self

        elif critere_tri == 3:
            # Si le bien à supprimer est plus petit que la racine, il est à gauche
            if bien_immo.surf < self.racine.surf:
                self.gauche = self.gauche.suppression(bien_immo, critere_tri)

            # Si le bien à supprimer est plus grand que la racine, il est à droite
            elif bien_immo.surf > self.racine.surf:
                self.droit = self.droit.suppression(bien_immo, critere_tri)

            # Si le bien n'est pas le bon, de part la manière dont fonctionne la classe ABR, le bien sera alors à droite
            elif not (bien_immo.nom == self.racine.nom and bien_immo.nat == self.racine.nat and bien_immo.surf == self.racine.surf and bien_immo.pmoy == self.racine.pmoy):
                self.droit = self.droit.suppression(bien_immo, critere_tri)

            # Si le bien à supprimer est égal à la racine
            else:
                # Cas 1 : Pas d'enfant gauche
                if self.gauche is None:
                    temp = self.droit
                    self = None
                    return temp
                # Cas 2 : Pas d'enfant droit
                elif self.droit is None:
                    temp = self.gauche
                    self = None
                    return temp
                # Cas 3 : Le bien à supprimer a deux enfants
                temp = self.valeur_noeud_minimum(self.droit)
                self.racine = temp.racine
                self.droit = self.droit.suppression(temp.racine, critere_tri)
            
            return self

        elif critere_tri == 4:
            # Si le bien à supprimer est plus petit que la racine, il est à gauche
            if bien_immo.pmoy < self.racine.pmoy:
                self.gauche = self.gauche.suppression(bien_immo, critere_tri)

            # Si le bien à supprimer est plus grand que la racine, il est à droite
            elif bien_immo.pmoy > self.racine.pmoy:
                self.droit = self.droit.suppression(bien_immo, critere_tri)
            
            # Si le bien n'est pas le bon, de part la manière dont fonctionne la classe ABR, le bien sera alors à droite
            elif not (bien_immo.nom == self.racine.nom and bien_immo.nat == self.racine.nat and bien_immo.surf == self.racine.surf and bien_immo.pmoy == self.racine.pmoy):
                self.droit = self.droit.suppression(bien_immo, critere_tri)
            
            # Si le bien à supprimer est égal à la racine
            else:
                # Cas 1 : Pas d'enfant gauche
                if self.gauche is None:
                    temp = self.droit
                    self = None
                    return temp
                # Cas 2 : Pas d'enfant droit
                elif self.droit is None:
                    temp = self.gauche
                    self = None
                    return temp
                # Cas 3 : Le bien à supprimer a deux enfants
                temp = self.valeur_noeud_minimum(self.droit)
                self.racine = temp.racine
                self.droit = self.droit.suppression(temp.racine, critere_tri)
            
            return self

    def valeur_noeud_minimum(self, racine):
        """
        Find the node with the minimum value in the binary search tree.

        Args:
            racine: The root node of the binary search tree.

        Returns:
            object: The node with the minimum value.
        """
        actuel = racine

        # Trouver le noeud le plus à gauche (le plus petit)
        while actuel.gauche is not None:
            actuel = actuel.gauche

        return actuel
    
    def afficher(self):
        """
        Display the binary search tree using inorder traversal.
        """
        if self.gauche:
            self.gauche.afficher()
        print(f"Nom: {self.racine.nom}, Nature: {self.racine.nat}, Surface: {self.racine.surf} m2, Prix moyen: {self.racine.pmoy} euros au m2")
        if self.droit:
            self.droit.afficher()

class Application:
    """
    A class representing the application for managing real estate properties.

    Attributes:
        root (tk.Tk): The root window of the application.
        bien_selectione (Bien_immo): The currently selected real estate property.
        biens (ABR): The binary search tree containing the real estate properties.
        critere_tri (int): The criteria used for sorting the properties.
    """

    def __init__(self, root):
        """
        Initializes the Application class.

        Args:
            root (tk.Tk): The root window of the application.
        """
        self.root = root
        self.root.title("Gestion des biens immobiliers")

        # Variables
        self.bien_selectione = None
        self.biens = ABR(None)
        self.critere_tri = 1 # trier par déffaut selon le nom

        # Importer les données
        donnees = importer_fichier_csv("data.csv")
        self.importe_donnees(donnees)
        
        # Interface utilisateur
        self.create_widgets()

    def importe_donnees(self, donnees):
        """
        Imports data into the application.

        Args:
            data (list): The list of real estate property data to import.
        """
        for nom, nature, prix_moyen, surface in donnees:
            bien = Bien_immo(nom, nature, surface, prix_moyen)
            self.ajouter_bien(bien)

    def supprimer_bien(self, bien):
        """
        Removes a real estate property from the application.

        Args:
            property_data (Bien_immo): The real estate property to remove.
        """
        if not bien: return

        if self.critere_tri == 5:
            afficher_erreur("Désolé, il est impossible de supprimer un bien lorsque les biens sont triés selon la nature.")
            return
        
        self.biens.suppression(bien_immo=bien, critere_tri=self.critere_tri)
        self.update_property_list()

    def ajouter_bien(self, bien=None):
        """
        Adds a new real estate property to the application.

        Args:
            property_data (Bien_immo, optional): The real estate property to add. If not provided, prompts the user to enter the property details.
        """
        # Si on connais déjà le bien alors on l'ajoute directement
        if bien:
            self.biens.insertion(bien_immo=bien, critere_tri=self.critere_tri)
            return
        
        # Sinon, on demande à l'utilisateur d'entrer les informations de celui-ci
        
        # Boîtes de dialogue pour saisir les informations sur le nouveau bien
        nom = sd.askstring("Nouvelle propriété", "Nom du bien immobilier:").strip()
        nature = sd.askstring("Nouvelle propriété", "Nature du bien (Maison, Appartement, Terrain, etc.):").strip()
        surface = sd.askstring("Nouvelle propriété", "Surface (en m²):").strip()
        prix_moyen = sd.askstring("Nouvelle propriété", "Prix moyen au m2 (en €):").strip()

        # Conditions pour vérifier les entrées utilisateur
        # Retire les espaces inutiles et converti les valeurs au bon format

        if not (nom and nature and surface and prix_moyen):
            afficher_erreur("Les entées ne doivent pas être vide.")
            return

        try:
            surface, prix_moyen = float(surface.replace(',', '.')), float(prix_moyen.replace(',', '.'))
        except:
            afficher_erreur("La surface et le prix moyen doivent être des nombres flottant.")
            return
        
        # Vérifie si la surface est positive
        if surface and surface <= 0:
            afficher_erreur("La surface doit être positive.")
            return

        # Vérifie si le prix moyen au mètre carré est positif    
        if prix_moyen and prix_moyen <= 0:           
            afficher_erreur("Le prix moyen au mètre carré doit être positif.")
            return
        
        # Si tout les test sont passés
        # Créer un objet Bien_immo avec les informations saisies
        bien = Bien_immo(nom, nature, surface, prix_moyen)
          
        # Ajouter le nouveau bien à la liste des propriétés
        self.biens.insertion(bien_immo=bien, critere_tri=self.critere_tri)

        # Mettre à jour la liste des biens dans l'interface utilisateur
        self.update_property_list()

    def importer_biens(self, fichier):
        """
        Imports real estate properties from a CSV file.

        Args:
            file_path (str): The path to the CSV file containing the property data.
        """
        donnees = importer_fichier_csv(fichier)
        for bien in donnees:
            self.ajouter_bien(bien)

    def trier_biens(self):
        """Sorts the properties based on the selected criteria."""
        if not self.biens: return # Si la liste des biens est vide, alors on ne tri pas

        liste_biens = self.biens.parcours_infixe()
        abr = ABR(liste_biens[0])
        for bien in liste_biens[1:]:
            abr.insertion(bien, self.critere_tri)

        self.biens = abr
        self.update_property_list()

    def bouton_tri(self, critere):
        """
        Sets the sorting criterion and sorts the properties accordingly.

        Args:
            criterion (int): The sorting criterion.
        """
        self.critere_tri = critere
        self.trier_biens()

    def create_widgets(self):
        """Creates the user interface widgets."""
        # Cadre principal
        main_frame = tk.Frame(self.root)
        main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Cadre de la liste des biens
        property_list_frame = tk.Frame(main_frame, width=250)
        property_list_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Liste des biens
        property_list_label = tk.Label(property_list_frame, text="Liste des biens", bg="#888888")
        property_list_label.pack(pady=(0, 10))

        self.property_listbox = tk.Listbox(property_list_frame, selectmode=tk.SINGLE, bg="#dddddd")
        self.property_listbox.pack(expand=True, fill=tk.Y)
        self.update_property_list()

        # Créer un cadre pour les deux premiers boutons
        buttons_frame1 = tk.Frame(property_list_frame)
        buttons_frame1.pack()

        # Ajouter les deux premiers boutons dans le premier cadre
        add_button = tk.Button(buttons_frame1, text="Ajouter", command=lambda: self.ajouter_bien(), bg='#66ff66')
        add_button.pack(side=tk.LEFT, padx=5, pady=5)

        remove_button = tk.Button(buttons_frame1, text="Supprimer", command=lambda: self.supprimer_bien(self.bien_selectione), bg="#ff6666")
        remove_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Créer un cadre pour les trois derniers boutons
        buttons_frame2 = tk.Frame(property_list_frame, bg="#6699ff")
        buttons_frame2.pack()

        # Ajouter les trois derniers boutons dans le second cadre
        sort1_button = tk.Button(buttons_frame2, text="Trier par nom", command=lambda: self.bouton_tri(1))
        sort1_button.pack(side=tk.LEFT, padx=5, pady=5)

        sort2_button = tk.Button(buttons_frame2, text="Trier par nature", command=lambda: self.bouton_tri(2))
        sort2_button.pack(side=tk.LEFT, padx=5, pady=5)

        sort3_button = tk.Button(buttons_frame2, text="Trier par surface", command=lambda: self.bouton_tri(3))
        sort3_button.pack(side=tk.LEFT, padx=5, pady=5)

        sort4_button = tk.Button(buttons_frame2, text="Trier par prix moyen", command=lambda: self.bouton_tri(4))
        sort4_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Cadre d'affichage des détails du bien
        property_details_frame = tk.Frame(main_frame)
        property_details_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Détails du bien sélectionné
        property_details_label = tk.Label(property_details_frame, text="Détails du bien", bg="#888888")
        property_details_label.pack(pady=(0, 10))

        self.property_details_text = tk.Text(property_details_frame, height=10, width=50, wrap=tk.WORD, bg="#dddddd")
        self.property_details_text.pack(expand=True, fill=tk.BOTH, pady=25, padx=5)

        # Associer la fonction de mise à jour des détails lors de la sélection d'un bien
        self.property_listbox.bind('<<ListboxSelect>>', self.update_property_details)

    def update_property_list(self):
        """
        Updates the list of real estate properties displayed in the GUI.

        This function clears the current listbox displaying properties and then inserts
        each property name in the listbox in infix order.

        """
        self.property_listbox.delete(0, tk.END)
        for bien in self.biens.parcours_infixe():
            self.property_listbox.insert(tk.END, bien.nom)

    def update_property_details(self, event):
        """
        Update the displayed details of the selected property.

        Args:
            event (tkinter event): The event generated when selecting a property from the list.
        """
        biens = self.biens.parcours_infixe()
        selected_index = self.property_listbox.curselection()

        if selected_index:
            index = selected_index[0]
            self.bien_selectione = biens[index]
            details_text = f"Nom: {self.bien_selectione.nom}\nNature: {self.bien_selectione.nat}\nSurface: {self.bien_selectione.surf} m²\nPrix au m²: {self.bien_selectione.pmoy} €\nEstimation: {round(self.bien_selectione.estimation())}€"
            self.property_details_text.delete(1.0, tk.END)
            self.property_details_text.insert(tk.END, details_text)

def importer_fichier_csv(nom_fichier):
    """
    Import data from a CSV file.

    Args:
        nom_fichier (str): The path to the CSV file.

    Returns:
        list: A list of tuples containing the imported data.
    """
    liste_biens = []
    with open(nom_fichier, newline='') as csvfile:
        lecteur_csv = csv.reader(csvfile, delimiter='\t')
        next(lecteur_csv)  # Ignorer l'en-tête
        for ligne in lecteur_csv:
            nom_bien_immobilier, nature, prix_moyen_m2, surface = ligne[0].split(";")
            prix_moyen_m2 = float(prix_moyen_m2.replace(',', '.'))  # Remplacer la virgule par un point pour les nombres décimaux
            surface = float(surface.replace(',', '.'))
            liste_biens.append((nom_bien_immobilier, nature, prix_moyen_m2, surface))
    return liste_biens

def afficher_erreur(message):
    """
    Display an error message in a dialog box.

    Args:
        message (str): The error message to display.
    """
    # Créer une fenêtre principale cachée
    root = tk.Tk()
    root.withdraw()

    # Afficher la boîte de dialogue d'erreur
    sd.messagebox.showerror("Erreur", message)

    # Détruire la fenêtre principale (c'est-à-dire la boîte de dialogue)
    root.destroy()

root = tk.Tk()
app = Application(root)
root.mainloop()