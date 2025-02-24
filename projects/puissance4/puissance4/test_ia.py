import gymnasium as gym
from stable_baselines3 import PPO
from puissance4Env import Puissance4Env

# Enregistrer l'environnement si nécessaire
gym.register(
    id="Puissance4-v0",
    entry_point="puissance4Env:Puissance4Env",
)

# Créer l'environnement
env = gym.make("Puissance4-v0")
# Créer le modèle PPO avec une politique de type MLP (Multi-Layer Perceptron)
model = PPO("MlpPolicy", env, verbose=1)

# Jouer contre l'IA
state, _ = env.reset()
done = False

while not done:
    # Tour du joueur humain
    print("C'est ton tour ! Choisis une colonne (0-6) :")
    human_action = int(input())  # Demande à l'utilisateur de choisir une colonne
    
    # Appliquer l'action du joueur humain
    state, reward, done, truncated, info = env.step(human_action)
    env.render()  # Affiche l'état actuel du jeu après l'action du joueur humain
    print(f"Récompense: {reward}, Jeu terminé: {done}")
    
    if done:
        break  # Si l'épisode est terminé, on sort de la boucle

    # Tour de l'IA
    print("C'est le tour de l'IA !")
    ai_action, _states = model.predict(state)  # L'IA choisit son action
    state, reward, done, truncated, info = env.step(ai_action)  # Applique l'action de l'IA
    env.render()  # Affiche l'état actuel du jeu après l'action de l'IA
    print(f"Récompense: {reward}, Jeu terminé: {done}")
