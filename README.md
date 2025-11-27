# AssaultCube Cheat (Python)

Un script de triche externe simple pour **AssaultCube** écrit en Python. Ce script utilise la bibliothèque `pymem` pour lire et écrire dans la mémoire du jeu afin de modifier la santé du joueur.

## 🚀 Fonctionnalités

- **Modification de la vie** : Fixe la santé du joueur à 9999.
- **Détection automatique** : Trouve automatiquement le processus `ac_client.exe`.
- **Pointeurs dynamiques** : Utilise des offsets pour localiser l'adresse de la santé en mémoire.

## 📋 Prérequis

Avant de lancer le script, assurez-vous d'avoir :

- **Python 3.x** installé sur votre machine.
- Le jeu **AssaultCube** installé et lancé.
- La bibliothèque Python **pymem**.

## 🛠️ Installation

1. Clonez ce dépôt ou téléchargez le fichier `ac_cheat.py`.
2. Installez les dépendances nécessaires via pip :

```bash
pip install pymem
```

## 🎮 Utilisation

1. **Lancez AssaultCube** et entrez dans une partie (ou le mode entraînement).
2. **Exécutez le script** Python :

```bash
python ac_cheat.py
```

3. Le script affichera les informations suivantes :
   - ID du processus du jeu.
   - Adresse de base du module.
   - Adresse du joueur et de la vie.
   - Confirmation que la vie a été modifiée.

4. Retournez en jeu et constatez que votre vie est passée à **9999** !

## ⚠️ Avertissement

Ce projet est à des fins **éducatives uniquement**. L'utilisation de logiciels de triche dans des jeux multijoueurs en ligne peut entraîner un bannissement. Utilisez ce script uniquement en mode solo ou sur vos propres serveurs.

## 📝 Structure du Code

- **Connexion au processus** : `Pymem("ac_client.exe")`
- **Calcul des adresses** : Utilisation de `lpBaseOfDll` et des offsets (`0x17E254`, `0xEC`).
- **Écriture mémoire** : `pm.write_int(health_address, 9999)`

## 📝 Comment est ce qu'on a trouvé les adresse : 
- **Cheat Engine** : On a commencé par lancer la fameux Cheat Engine, on a tapé la valeur de la vie dans la barre de recherche et on a chercher les adresse qui changeait quand on changeait la vie dans le jeu. 
- **Création de pointeur** Une fois avoir trouvé l'adresse de la vie de notre joueur, le soucis qu'il y'avait c'est que a chaque lancement du jeu une nouvelle allocation de memoire est faite, donc l'adresse de la vie changeait a chaque lancement du jeu. on a donc décidé de créer un pointeur pour trouver l'adresse de la vie de notre joueur. trouvé un offset qui changeait pas a chaque lancement du jeu.

- **Résultat** : Apres avoir trouvé l'offset qui changeait pas a chaque lancement du jeu, on a décidé de l'utiliser pour trouver l'adresse de la vie de notre joueur.

## 🕵️ Méthodologie de Recherche

- **Scan avec Cheat Engine** : Nous avons utilisé **Cheat Engine** pour scanner la mémoire du jeu. En filtrant la valeur de la santé du joueur après chaque modification (dégâts/soins), nous avons isolé l'adresse mémoire dynamique.
- **Pointer Scan** : L'adresse de la santé changeant à chaque redémarrage (allocation dynamique), nous avons effectué un "Pointer Scan" pour trouver une chaîne de pointeurs stable.
- **Résultat** : Identification d'un offset statique (`0x17E254`) par rapport à l'adresse de base du module, permettant une détection fiable à chaque lancement.

---
*Créé pour l'apprentissage du Game Hacking et de la manipulation mémoire en Python.*
