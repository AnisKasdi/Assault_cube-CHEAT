from pymem import Pymem # 
from pymem.process import module_from_name

# 1. Connexion au jeu
print("Recherche de AssaultCube...")
try:
    pm = Pymem("ac_client.exe") # recherche du via de le nom du processus 
    print(f"Jeu trouvé ! ID du processus : {pm.process_id}") # affiche l'id du processus
except:
    print("Erreur : Lance le jeu d'abord !") # gestion des erreurs
    exit()

# 2. Récupération de l'adresse de base (ac_client.exe)
game_module = module_from_name(pm.process_handle, "ac_client.exe").lpBaseOfDll
print(f"Base Address : {hex(game_module)}")

# --- CONFIGURATION DES OFFSETS ---
# Si ton adresse 0x17E254 ne marche pas, essaie 0x10F4F4 (Standard AC 1.2.0.2)
PLAYER_BASE_OFFSET = 0x17E254  
HEALTH_OFFSET = 0xEC           
# ---------------------------------

# 3. Calcul du Pointeur (Pointer Chain)
# On lit l'adresse du joueur à "Base + Offset"
try:
    # On va chercher l'adresse du LocalPlayer
    player_address = pm.read_int(game_module + PLAYER_BASE_OFFSET)
    print(f"Adresse du Joueur : {hex(player_address)}")

    # On calcule l'adresse finale de la vie
    health_address = player_address + HEALTH_OFFSET
    print(f"Adresse de la Vie : {hex(health_address)}")

    # 4. Lecture et Écriture
    current_health = pm.read_int(health_address)
    print(f"Vie actuelle : {current_health}")

    print("Modification de la vie à 9999...")
    pm.write_int(health_address, 9999)
    
    print("CHEAT ACTIVÉ ! Regarde ton jeu.")

except Exception as e:
    print(f"Une erreur est survenue (mauvais offset ?) : {e}")

input("Appuie sur Entrée pour quitter...")