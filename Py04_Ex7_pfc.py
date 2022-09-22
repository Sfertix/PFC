# -*- coding: utf-8 -*-
"""
    création : septembre 2022
    @auteur : Baptiste Boutorine (bboutorine)
    Version : 1.0 (for ECAD)
    Objectif : Jouer au pierre / feuille / ciseaux contre l'ordinateur
    Entrées: user_choice (type : int) : choix de l'utilisateur
    Sorties : result (type : string) : résultat du duel
"""
# Import du module
from random import choice

# Affichage des instructions classiques
print("Vous jouez au pierre / feuille / ciseaux contre l'ordinateur,"\
      " pour jouer vous devrez entrer un nombre du menu ci-dessous\n" \
      "\n\t1 - Pierre\n\t2 - Feuille\n\t3 - Ciseaux")

# Choix de l'utilisateur
user_choice = int(input("À vous de jouer : "))
computer_choice = choice([1,2,3])

# Bloc conditionnel : 
#   • if teste toutes les solutions qui permette à l'utilisateur de gagner
#   • elif teste une égalité
#   • else renvoie automatiquement la défaite de l'utilisateur
if (user_choice == 1 and computer_choice == 3) \
    or (user_choice == 2 and computer_choice == 1) \
    or (user_choice == 3 and computer_choice == 2):
    print("C'est gagné !")

elif user_choice == computer_choice:
    print("C'est une égaité !")

else:
    print("C'est une défaite")