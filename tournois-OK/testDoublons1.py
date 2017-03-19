# -*- coding: utf-8 -*-
#!/usr/bin/python3

## permet de tester des doublons dans une liste

from tkinter import *
import random 
from creationPoules import *


liste=[]
listeFinale =[]

nbListe =0

for i in range(0,50):
    
    hasard1 = random.randint(0,10)
    hasard2 = random.randint(0,10)
    ##print(i," ",hasard1," ",hasard2)
    liste.append([i,hasard1,hasard2])

print("nombre d'élément dans la liste créée:", len(liste),"\n")
print("Liste crée:", liste,"\n")

## prendre au hasard un element de la liste puis un second
## comparer si ils sont de la même region
## si oui alors en choisir un autre
## si non, le garder
a = b = c = d = []
listeTest =liste
listeOK =[]
k=0
a = random.choice(listeTest)
print ("premier choix:", a)
listeTest.remove(a)
listeOK.append(a)
z=1

while z < 4:
    b = random.choice(listeTest)
    print("choix suivant:",b,"\n")
    k=0
    for w in listeOK:
        if b[2] == w[2]:
            
            print ("Attention, même region:",b)
            k=1
            
        elif b[2] != w[2]:
            print("\n")
            print("OK les regions sont differentes: region 1, ",w[2],", region 2,",b[2])
            
            
            
    if k != 1:
        listeOK.append(b)
        listeTest.remove(b)
        z+=1
        
    print("\n""nombre d'éléments dans liste de test: ",len(listeTest))     
    print("liste test",listeTest)
    print("\n")
    print("nombre d'éléments dans liste OK: ",len(listeOK))
    print("liste OK",listeOK)
    print("\n")
      
    





#### faire la repartition dans des poules
#### la suite sert pour un affichage d'info et création des poules

##Repartition = creationPoule(nbListe, liste, effectifGroupe)  ## met le resultat des repartions par stade 
                                                                            #### dans une variable pour l'utiliser ensuite
                                                                            
##print(Repartition)  ##affiche les différentes repartition dans un dico avec comme clé le mot Stade1, Stade2, Stade3, Stade4


#### test des doublons en troisieme valeur

##nbGroupe = len(Repartition)


##print("\n", "Un dictionnaire n'étant pas classé, il faut le classer pour mieux le lire")
##print("\n","Classement des clés par ordre alphabétique")
##print(sorted(Repartition.items(), key=lambda t: t[0]))     ## affichage des stades avec les clés classées

##print("\n", "Un dictionnaire n'étant pas classé, il faut le classer pour mieux le lire")
##print("\n","Classement des clés par ordre numerique du premier caractère du contenu")
##print(sorted(Repartition.items(), key=lambda t: t[1]))     ## Classement des clés par ordre numerique du premier caractère du contenu


##print("\n","Classement")    
##for k, v in Repartition.items():
    ##print("Stade {} : {}".format(k, v))

### On récupère les cle pour les mettre dans une liste
##listeCle = {}
##for cle in Repartition:

    ##listeCle[cle] = Repartition[cle]
##listeCle = sorted(listeCle)
##print("liste des différents stade mis dans une liste: ",listeCle)

#### recuperation valeur dans dictionnaire
##for valeur in Repartition.values():
     ##print (valeur)

##print("Les valeurs dans le dico: ",Repartition.values())


