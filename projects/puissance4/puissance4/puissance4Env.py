import gymnasium as gym
from gymnasium import spaces
import numpy as np

class Puissance4Env(gym.Env):
    def __init__(self):
        super(Puissance4Env, self).__init__()

        # Dimensions de la grille
        self.rows = 8
        self.columns = 10
        self.grid = np.zeros((self.rows, self.columns), dtype=np.int32)  # Grille vide
        # Actions possibles : Choisir une colonne entre 1 et 10
        self.action_space = spaces.Discrete(self.columns)

        # L'état de la grille : 0 = vide, 1 = joueur 1, 2 = joueur 2
        self.observation_space = spaces.Box(low=0, high=2, shape=(self.rows, self.columns), dtype=np.int32)

        # Réinitialisation de la grille
        self.reset()

    def reset(self, seed=None, options=None):
        """Réinitialiser l'état du jeu."""
        super().reset(seed=seed)
        self.grid = np.zeros((self.rows, self.columns), dtype=np.int32)  # Grille vide
        self.done = False
        self.current_player = 1  # Le joueur 1 commence
        return self.grid, {}

    def step(self, action):
        """Effectuer un coup."""
        # Vérifie si l'action est valide
        if self.grid[0, action] != 0:
            return self.grid, -10, True, False, {}  # Colonne pleine, retour de pénalité

        # Placer le jeton du joueur dans la colonne choisie
        for row in range(self.rows - 1, -1, -1):
            if self.grid[row, action] == 0:
                self.grid[row, action] = self.current_player
                break

        # Vérifie la victoire
        if self.check_victory():
            return self.grid, 10, True, False, {}  # Victoire, retour de récompense

        # Vérifie si c'est un match nul
        if np.all(self.grid != 0):
            return self.grid, 0, True, False, {}  # Match nul

        # Changer de joueur
        self.current_player = 3 - self.current_player  # Alterne entre 1 et 2

        return self.grid, 0, False, False, {}  # Continuer le jeu


    def check_victory(self):
        """Vérifie si un joueur a gagné."""
        # Vérification horizontale
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if all(self.grid[row, col + i] == self.current_player for i in range(4)):
                    return True

        # Vérification verticale
        for row in range(self.rows - 3):
            for col in range(self.columns):
                if all(self.grid[row + i, col] == self.current_player for i in range(4)):
                    return True

        # Vérification diagonale
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if all(self.grid[row + i, col + i] == self.current_player for i in range(4)):
                    return True
            for col in range(3, self.columns):
                if all(self.grid[row + i, col - i] == self.current_player for i in range(4)):
                    return True

        return False

    def render(self):
        """Affiche la grille."""
        for row in self.grid:
            print(" | ".join(str(x) if x != 0 else "." for x in row))
            print("-" * (self.columns * 4 - 1))
