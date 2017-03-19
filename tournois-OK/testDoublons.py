# -*- coding: utf-8 -*-
#!/usr/bin/python3

## permet de tester des doublons dans une liste

from tkinter import *
import random 
import csv
#from creationPoules import *
#from functools import partial ## permet dans un bouton d'avoir une commande avec des variable
 




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

def creationPoule1(nbequipe,effectifPoule):
    ##effectifPoule = 4
    StadeEquipes = {} 
    
    listeEquipesStade=[]
    
    nbStade = int(nbequipe/effectifPoule)  ##pour avoir le nombre de stade
    resteEquipe = nbequipe % effectifPoule    ## pour connaitre le nombre d'équipe qu'il reste 
                                            ## à repartir sur les derniers stade
                                            
    ## definir le nome d'equipes par stade
    
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
        
    return(listePoule)   ##récuperer la liste avec le nombred'equipes dans chaque poule
                                            
    ## fin definition du nombre d'équipe par stade
                                            
    



##


def creationStade1(listePoule, listeEquipe):
    
    ## création des stades a partir de la liste du nombre d'équipe par poule
    
    liste = listeEquipe
    listeFinale =[]
    
    nbListe =0
    StadeEquipesCreation = {}
    
    
    
    ## prendre au hasard un element de la liste puis un second
    ## comparer si ils sont de la même region
    ## si oui alors en choisir un autre
    ## si non, le garder
    
    
        
    i=0
    a = b = c = d = []
    poule = listePoule
    listeTest =liste
    listeOK =[]
    y = len(listePoule)  #compte le nombre de stade
    print(" NOMBRE DE STADE : ",y) 
    yy = y-1    ## yy = y-
        
    for q in poule[:y-1]:
        i+=1
        print(q)
        k=0
        a = random.choice(listeTest)
        print ("premier choix:", a)
        listeTest.remove(a)
        listeOK.append(a)
        z=1
    
    
        while z < q:   ## on fait q-1 pour tester la derniere poule qui peut avoir des équipe d'une même region'
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
        
        
            
            
        NumeroStade = (i) ## chaque stade a un numéro. 
                            ## Cela facilite le classement par ordre
                            ## dans d'autre partie du programme    
        ## creation de dictionnaires pour enregistrer les differents stades
        StadeEquipesCreation[NumeroStade] =  listeOK
        ## fin creation dictionnaires
        listeOK=[] 
        ##input("Appuyez sur ENTREE pour fermer ce programme...")        ### pour s'arreter à chaque passage et voir le problème
    
    for g in poule[:-1]:  ## pour la derniere poule avec de possible regions identiques
        listeOK = listeTest 
        NumeroStade = i+1
        StadeEquipesCreation[NumeroStade] =  listeOK
        print(g)              
    
    for cle, valeur in StadeEquipesCreation.items():

        print("Le stade {} contient les équipes suivante\n {}.".format(cle, valeur),"\n")
        
    return(StadeEquipesCreation)

if __name__ == "__main__":
    
    effectifPoule = 4
    
    importDeptSelect()       ## importer le fichier sur lequel on travail
    NbEquipe=int(len(SelectDept)) ## calcul le nombre d équipes selectionnées 
      
    orgaPoule= creationPoule1(NbEquipe,effectifPoule)      ## calcul le nombre d'équipe par poule 
                                                ## et donc la création des poules
    
    print("nombre d'équipe: ",NbEquipe, "\n")
    print("Liste des équipes: ",SelectDept,"\n")
    print("Organisation des poules: ",orgaPoule,"\n")
    
    
    StadeRepartition = creationStade1(orgaPoule, SelectDept)  ## création des poules avec les equipes
                                            ## test pour ne pas avoir de même region dans une poule
    
    #print("equipes par stade\n",StadeRepartition)
    
    
      
    





