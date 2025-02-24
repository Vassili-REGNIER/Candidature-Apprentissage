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
model = PPO("MlpPolicy", env, learning_rate=1e-4, batch_size=64, gamma=0.99, ent_coef=0.01, verbose=1)

# Entraîner le modèle avec 10 000 timesteps
model.learn(total_timesteps=1000000)

# Sauvegarder le modèle après l'entraînement
model.save("puissance4_model")
