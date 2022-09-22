# -*- coding: utf-8 -*-
"""
    Création : Septembre 2022
    @auteur : Baptiste Boutorine (bboutorine)
    Version : 2.0
    Objectif : Jouer au pierre / feuille / ciseaux contre l'ordinateur
    Entrées : user_choice (type : int) : choix de l'utilisateur
    Sorties : result (type : string) : résultat du duel
"""
from random import choice
from colorama import Fore, init  # Module de coloration de texte en console

init(autoreset=True)

# Différentes variables globales
game_element = {1: "✊ Pierre", 2: "✋ Feuille", 3: "✌️ Ciseaux"}

print("Vous jouez au pierre / feuille / ciseaux contre l'ordinateur," \
      " pour jouer vous devrez entrer un nombre du menu ci-dessous")

# Fonction 'get_choices' - Récupère le choix de l'utilisateur
def get_choices():
    print("\n\t1 - Pierre\n\t2 - Feuille\n\t3 - Ciseaux")
    user_choice = int(input("À vous de jouer : "))

    if user_choice not in [1, 2, 3]:
        print(f"{Fore.RED} Entrée invalide")
        get_choices()

    else:
        computer_choice = choice([1, 2, 3])
        check_result(user_choice, computer_choice)


# Fonction 'check_result' - Détermine qui a gagné
def check_result(user_choice: int, computer_choice: int):
    if (user_choice == 1 and computer_choice == 3) \
            or (user_choice == 2 and computer_choice == 1) \
            or (user_choice == 3 and computer_choice == 2):
        print(f"+1 pour vous : (vous) {game_element[user_choice]} - {game_element[computer_choice]} (ordinateur)")
        user_score += 1

    elif user_choice == computer_choice:
        print("C'est une égalité !")

    else:
        print(f"+1 pour l'ordinateur : (vous) {game_element[user_choice]} - {game_element[computer_choice]} (ordinateur)")
        computeur_score += 1

get_choices()
