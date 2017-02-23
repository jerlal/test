# -*- coding: utf-8 -*-
#!/usr/bin/python3
from tkinter import *
import csv
import random
import csv
from functools import partial ## permet dans un bouton d'avoir une commande avec des variable
import scrollbarJerome  ##programme jerome permettant d'integrer une scrollbar H ou V  ,  à essayer d integrer
from fenetreMultiplesStade import *

## pour afficher les differents stades

poules={}
SelectDept=[]
StadeEquipes = {}       ## creation d un dictionnaire pour enregistrer les equipes par stade
listeEquipes =[]        ## pour créer des liste d' équipe par stade



def importDeptSelect():
    fileDept = csv.reader(open('DeptSelect.csv', 'r'))
    # listeDept est la liste des departements avec le numéro et la région
    for row in fileDept:
        ##SelectDept.append([row[0], row[1], row[2]])  #ancienne version
        SelectDept.append([row[0], row[1], row[2],0])     ## nouvelle version modif jerome  pour integrer des colonnes vides pour resultats
                                                                    ## À modifier pour adapter en fonction du nombre d'équipe par stade definie au départ'



 




class Stade:
    ##def __init__(self, ligne, colonne):
    
    def __init__(self,stade):
        fen2=Tk()
        fen2.title('Répartition stade avec les '+str(len(SelectDept))+' équipes sélectionnées')
        fen2.geometry("1200x900")
        fen2.config(bg="white")
        
        
        fen2.minsize(400, 300) ## taille minimum de la fenetre
        fen2.maxsize(1200,900) ## taille maximum de la fenetre
        fen2.positionfrom("user") ## placement manuel de la fenetre
        fen2.sizefrom("user") ## dimensionnement manuel de la fenetre
        
        
        s=0
        k=0
        l=0
        j=0
        ligneNumero=0
        colonnePosition=0           #permet de mettre les colonnes en dessous si dépassement du nombre maxi de colonne par ligne
        NbColonneMax=4              # nb de colonne maxi par ligne pour affichage

        listeEquipes =[]   
        colonne=4
        print("Nombre de stades: ",len(stade))
        print("\n")
        print (" tournois avec la repartition suivante: \n ")
        print (stade)
       
        
        # affichage des colones pour les stades
        while k < (len(stade)):
            
            NumeroStade = ('Stade'+str(k+1))          ## nom et numero du stade
                                                    ## qui sert de clé dans 
                                                    ## le dictionnaire stade indiqué en variable dans la def
                                                    
            
            StadeEquipes = stade                    ## StadeEquipes est le dictionnaire
            
            ligne = len(stade[NumeroStade])
            print("NOMBRE D'EQQUIPE SUR LE",NumeroStade,": ",ligne)
            
            
            ####pour le bouton, la command = partial (....) permet de rajouter des variable à la commande
            #### ne pas oublier de faire l'import de functools
            #### si on clique sur le nom du stade qui est un bouton, une autre fenetre s'ouvre avec le nom du stade
            
            Button(fen2, text=NumeroStade,command=partial(nouvelle_fenetre, NumeroStade, stade), width=30, height=1,bg='#aa0000',fg='white').grid(row=0+ligneNumero, column=colonnePosition, sticky=NSEW)  # titre de la colonne incrementée de 1 à chaque fois
                                                                                               
            
            while j < ligne and s < NbEquipe:   # le test de s évite les erreurs de dépassement du nombre d équipes'
                ##NumEquipe=X[s]
                
                
                ##textAffichage = (str(Dept[NumEquipe][0])+" "+str(Dept[NumEquipe][2]))
                
                listeEquipes=stade[NumeroStade]  # mettre dans une liste 'equipes'' la liste du dico 'StadeEquipe' qui a la clée 'variable'
                
                textAffichage = (listeEquipes[j][0])
                txt1 = Label(fen2, text = textAffichage, width=30, height=1) 
                
                
                txt1.config(relief=GROOVE, bd=2,fg="black",bg="white",font="Courier 8",)
               
                txt1.grid(row=j+1+ligneNumero, column=colonnePosition, sticky=NSEW) 
                       
                
                s+=1
                
                j+=1
            
            j=0
            k+=1
            
            colonnePosition+=1
            if k==NbColonneMax or k==2*NbColonneMax or k==3*NbColonneMax or k==4*NbColonneMax or k==5*NbColonneMax:
                ligneNumero+=20        ## permet d'afficher toutes les equipes dans les case stade
                colonnePosition=0
                
                
            

       
       

        Button(fen2, text='Suivant', command=fen2.destroy).grid(row = 50, column = 1,  padx =0, pady =0, sticky =NSEW)
        
        fen2.mainloop()
 
# départ de l'affichage des listes par stade :
if __name__ == "__main__":
    
    from creationPoules import *
    
    print("\n PREMIER TOUR \n")
    
    effectifPoule = 4
    importDeptSelect()  ## importer le fichier sur lequel on travail
    NbEquipe=int(len(SelectDept)) #calcul le nombre d équipes selectionées
    
    print("\n MELANGE DES EQUIPES \n")
    
    X = [i for i in range(0, NbEquipe)]  ## la séquence qui sera battue. Chiffre de 0 à Nombre d'équipe -1
     
    Battre(X)                           ## melange avec la def Battre créée au debut
    
    print("\n CRÉATION DES POULE ET DU DICO STADE \n")
    
    StadeRepartition = creationPoule(NbEquipe,X,SelectDept,effectifPoule)  ## met le resultat des repartions par stade 
                                                                            ## dans une variable pour l'utiliser ensuite
    print("equipes par stade\n",StadeRepartition)
    
    Stade(StadeRepartition)
   
    
