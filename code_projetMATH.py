#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 12:34:56 2022

Author : Regina, Doruntina, Eirini et Marina

"""

import re # on importe la librairie des regex
import os # on importe la librairie pour manipuler des fichiers

corpus = open("math_corpus.txt","r") # on ouvre le fichier des énoncés en mode lecture
corpus = corpus.readlines() # on stocke les lignes dans une variable corpus

# on crée nos listes de termes d'indices d'opérations ambigus
addition = ['plus', 'somme']
soustraction = ['différence','moins','néanmoins']
division = ['séparer','sépare','chacun', 'chacune', 'par', 'en','moyenne']
multiplication = ['produit','fois', 'chacun', 'chacune','moyenne']

file_resultats = open("resultat_corpus.txt", "w") # on crée un fichier
      
def traitement(texte): # on crée une fonction traitement
    enonces = set() # on crée un set vide énoncés
    # on incrémente plusieurs compteurs :
    e = 0 # compteur phrases
    nb_add = 0 # compteur addition
    nb_sous = 0 # compteur soustraction
    nb_div = 0 # compteur division
    nb_mult = 0 # compteur multiplication
    # -----------------------------------------------
    for phrases in texte: # pour chaque phrase du texte
        e+=1 # on ajoute 1 à e (= nombre d'énoncés, énumération fichier)
        if phrases not in enonces: # si l'énoncé lu n'est pas dans le set d'énoncés
            enonces.add(phrases) # on l'ajoute au set (= permet d'éviter les doublons)
            file_resultats.write(f"\n{e} : {phrases}\n") # et on écrit l'énoncé dans le fichier
            for mot in re.split("\W+",phrases): # pour chaque mot (grâce à la regex) de l'énoncé
                # -----------------------------------------------
                if mot in addition: # si le mot est dans la liste addition
                    file_resultats.write(f"Mot retrouvé : {mot} --> Addition !\n") # on écrit dans le fichier le terme trouvé
                    nb_add+=1 # et on ajoute 1 au nombre de termes d'addition
                # -----------------------------------------------                
                if mot in soustraction: # si le mot est dans la liste soustraction
                    file_resultats.write(f"Mot retrouvé : {mot} --> Soustraction !\n") # on écrit dans le fichier le terme trouvé
                    nb_sous+=1 # et on ajoute 1 au nombre de termes de soustraction
                # -----------------------------------------------                
                if mot in division: # si le mot est dans la liste division
                    file_resultats.write(f"Mot retrouvé : {mot} --> Division !\n") # on écrit dans le fichier le terme trouvé
                    nb_div+=1 # et on ajoute 1 au nombre de termes de division
                # -----------------------------------------------               
                if mot in multiplication: # si le mot est dans la liste multiplication
                    file_resultats.write(f"Mot retrouvé : {mot} --> Multiplication !\n") # on écrit dans le fichier le terme trouvé
                    nb_mult+=1 # et on ajoute 1 au nombre de termes de multiplication
        else: # si la phrase est déjà dans le set
        	break # on arrête
    # et on affiche nos compteurs
    print('Termes "addition" : ',nb_add)
    print('Termes "soustraction" : ',nb_sous)
    print('Termes "division" : ',nb_div)
    print('Termes "multiplication" : ',nb_mult)
    print(len(enonces))

                
traitement(corpus) # on appelle notre fonction sur le corpus
file_resultats.close() # on ferme le fichier de resultats créé

'De Paris à Orléans il y a 120 km. D’Orléans à Bourges il y a 110 km. De Bourges à Montluçon il y a 92 km. Quelle distance sépare Paris de Montluçon ? \n'
'De Paris à Orléans il y a 120 km. D’Orléans à Bourges il y a 110 km. De Bourges à Montluçon il y a 92 km. Quelle distance sépare Paris de Montluçon ?\n'

output_ent = open("output_entites_unitex.txt","r") # on ouvre le fichier des énoncés en mode lecture
output_ent = output_ent.readlines() # on stocke les lignes dans une variable output
liste_ent = open("noms_villes_communs.txt","r") # on ouvre le fichier des énoncés en mode lecture
liste_ent = liste_ent.readlines() # on stocke les lignes dans une variable output
print(type(liste_ent))
stop_list = open("stopwords-fr.txt","r")
stop_list = stop_list.readlines()
print(str(stop_list))


def compteur_ambigu(texte):
    nb = 0
    lis = []
    for phrases in texte:
        #print(phrases)
        for mot in re.split("\W+",phrases):
            #print(mot)
           if mot not in liste_ent and mot.istitle() :
                lis.append(mot)
                nb+=1
    #print(nb)
    #print(lis)
    for word in stop_list:
        mot = word.replace('\n', '')
        #print(stop_list)
        for word in lis:
            if mot == word and mot in stop_list:
            #print(word.islower())
            #print(mot)
            #print(mot.islower())
                lis.remove(mot)
    print(len(lis))
    #print(lis)

#compteur_ambigu(output_ent)

#print(type(stop_list))
