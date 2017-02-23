#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

##affichage d'une fenetre fille en cliquant sur un bouton

from functools import partial ## permet dans un bouton d'avoir une commande avec des variable
from tkinter import * 
import random
import csv
from functools import partial ## permet dans un bouton d'avoir une commande avec des variable

##from fenetreMultiplesStade import *

SelectDept=[]
s=0
k=0
l=0
j=0
ligneNumero=0
colonnePosition=0           #permet de mettre les colonnes en dessous si dépassement du nombre maxi de colonne par ligne
NbColonneMax=4              # nb de colonne maxi par ligne pour affichage
Col=0

def importDeptSelect():
        fileDept = csv.reader(open('DeptSelect.csv', 'r'))
        # listeDept est la liste des departements avec le numéro et la région
        for row in fileDept:
            ##SelectDept.append([row[0], row[1], row[2]])  #ancienne version
            SelectDept.append([row[0], row[1], row[2],0])     ## nouvelle version modif jerome  pour integrer des colonnes vides pour resultats
                                                                        ## À modifier pour adapter en fonction du nombre d'équipe par stade definie au départ'

def Battre(L): 
        #"""Mélanger""" 
        return random.shuffle(L)    

def creationPoule(nbequipe,listeMelange,listeEquipe,effectifPoule):
    ##effectifPoule = 4
    StadeEquipes = {} 
    
    listeEquipesStade=[]
    
    nbStade = int(nbequipe/effectifPoule)  ##pour avoir le nombre de stade
    resteEquipe = nbequipe % effectifPoule    ## pour connaitre le nombre d'équipe qu'il reste 
                                            ## à repartir sur les derniers stade
                                            
    ## definir le nome d'eqipes par stade
    
   ## À partir d'un liste de joueurs, determiner  combien de poules de 
    ##  il ne doit pas rester de poule avec moins de joueurs que le nombre defini
    ## Ils seront repartis dans les dernière poule qui auront plus de joueurs chacune 
    
    print(" le nombre d'équipe au total: ", nbequipe)
    
    
    
    
    print("le Nombre de joueur par poule: ", effectifPoule)
    
    
    
    
    
    ##faire des poules  
    
    
    nbPoule = ( nbequipe / effectifPoule)
    reste = nbequipe % effectifPoule
    poule4 = 0
    poule5 = 0
    listePoule =[]
    k = 0 
    l = 0
    z = 0
    #print("poule de ",effectifPoule," joueurs: ",int(nbPoule),"\n")
    
    print ("il y a ",int(nbPoule)," poules de ",effectifPoule," joueurs")
    
    if reste != 0:
                                 
        ##indique combien il reste de joueurs qui ne sont pas dans les poules
        
        print(" mais reste ",reste, "joueurs","\n")
    
    if  nbPoule - reste == 0 or reste == 0: 
                
        ## si le nombre total d'equipe est divisible par le nombre d'equipe par poule
        
        print ("il y aura  ",int(nbPoule)," poules de ",effectifPoule," joueurs ")
        
        ## creation de la liste avec effectif dans chaque poule
        
        while k < (int(nbPoule)):
            listePoule.append(effectifPoule)
            k+=1
        print("liste du nombre d'equipe sur chaque stade: ",listePoule)
        
    elif nbequipe <= effectifPoule or nbPoule < 2:
        
        ## si il n'y a pas assez d'equipe pour faire plusieurs poule
        
        print("il n'y aura qu'une poule de ",nbequipe,"joueurs")
        ## creation de la liste avec effectif dans chaque poule
        listePoule.append(nbequipe)
        
    elif nbPoule > reste:
    
        ## indique le nombre de poule avec le nombre d'equipe dans chacune
        ## certaine ont le bon nombre dans leurs poule et d'autre en ont une de plus
        
        poule = int(nbPoule -reste)
        poule5 = int(nbPoule - poule)
        print ("donc en fait il y aura ",poule,"poules de ",effectifPoule," et ",poule5," poules de ",(effectifPoule + 1) )
        ## creation de la liste avec effectif dans chaque poule
        
        while k < poule:
            listePoule.append(effectifPoule)
            k+=1
        while l < poule5:
            listePoule.append(effectifPoule +1)
            l+=1
        print("liste du nombre d'equipe sur chaque stade: ",listePoule)
    
    elif reste > (nbPoule/2):
        
        ## nombre d'équipe dans chaque poule avec des valeurs qui ne correspondent pas au nombre définit au départ (cas particuliers)
        
        poule1 = int(nbequipe/2)
        poule2 = nbequipe-poule1
        if poule1 == poule2:
            print("il y aura 2 poules de ",poule1," joueurs")
            while k < 2:
                listePoule.append(poule1)
                k+=1
        else:
            print ("il y aura une poule de ",poule1, " joueurs et une poule de ",poule2," joueurs")
            listePoule = [poul1,poule2]
            
        print("liste du nombre d'equipe sur chaque stade: ",listePoule)
                                            
    ## fin definition du nombre d'équipe par stade
                                            
    print("nombre d'équipe: ",nbequipe, "\n")
    print("Liste mélangée: ",listeMelange,"\n")
    print("liste des equipes: ")
    print(str(listeEquipe)+"\n")
    print("liste du nombre d'equipe sur chaque stade: ",listePoule)
    ##print("Effectif par poule (ou stades): ",effectifPoule)
    
    
    ##print(" nombre de stade:  ",nbStade,"\n")
    ##print ("reste sur dernier stade:  ",resteEquipe,"\n")
    
    i=0     ## pour les boucles suivantes avec while
    w=0     ## pour les boucles suivantes avec while
    
    ## peut etre déterminer ici le nombre d'equipe par stade
    ## puis ensuite faire des boucles qui prenne le nombre d'équipe dans chaque poule
    
    ##while i< int(nbStade-resteEquipe):                  
    
    ## création d'un dictionnaire  avec des équipes sur chaque stade
    
    y = len(listePoule)     #compte le nombre de stade
    print(" NOMBRE DE STADE : ",y)                                                
    while i < y:                                                    
        NumeroStade = ('Stade'+str(i+1))
        j = 0
        ##for j in (range(0+w,effectifPoule+w)):
        while j < (listePoule[i]):
            NumEquipe = listeMelange[z]
            ##print(NumEquipe)              ##pour verifier
            #print(NumeroStade,NumEquipe)   ##pour verifier
            
            ### creation liste equipe par stade
            listeEquipesStade.append(listeEquipe[NumEquipe])
        
            ###fin création liste equipe par stade
            z+=1
            j+=1
        ##print(NumeroStade,": ",listeEquipesStade) ##pour verifier
        
            
        ### creation de dictionnaires pour enregistrer les differents stades
        StadeEquipes[NumeroStade] =  listeEquipesStade
        ### fin creation dictionnaires
        listeEquipesStade=[]
        #print ("liste des equipe sur le ",NumeroStade,": ",listeEquipesStade)
        i+=1
        w+=effectifPoule
        
    
    ##print(StadeEquipes)
    return(StadeEquipes)
    
    
   


if __name__ == "__main__":
    
    fenetre = Tk() 
      
    fenetre.title("Fenêtre principale") 
                
    
    StadeEquipes = {}       ## creation d un dictionnaire pour enregistrer les equipes par stade
    listeEquipes =[]        ## pour créer des liste d' équipe par stade
    effectifPoule =4
    
    
    
    
    importDeptSelect()  ## importer le fichier sur lequel on travail
    NbEquipe=int(len(SelectDept)) #calcul le nombre d équipes selectionées   
    
    Col=int(((len(SelectDept)/effectifPoule)+0.9))  # permet de determiner le nombre de colonne 
                                        # le +0.9 permet de rajouter une colonne pour les 1, 2 ou 3 équipes restantes
                                        
    Dept=SelectDept 
   
    
    
    
    
    X = [i for i in range(0, NbEquipe)]  ## la séquence qui sera battue. Chiffre de 0 à Nombre d'équipe -1
     
    Battre(X)                           ## melange avec la def Battre créée au debut
    
    ## affichage pour info
    print("Les équipes: ",SelectDept)
    print("nb d'équipe sélectionnées:", len(SelectDept))
    print("réparties sur ", Col, "stades")
    print("le melange:  ",X) 
    
      
    StadeRepartition = creationPoule(NbEquipe, X, SelectDept, effectifPoule)  ## met le resultat des repartions par stade 
                                                            ## dans une variable pour l'utiliser ensuite
    print("equipes par stade\n",StadeRepartition)
    
    
    fenetre.mainloop()
