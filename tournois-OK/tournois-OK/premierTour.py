# -*- coding: utf-8 -*-
#!/usr/bin/python3
from tkinter import *
import csv
import random
import csv
from functools import partial ## permet dans un bouton d'avoir une commande avec des variable
import scrollbarJerome  ##programme jerome permettant d'integrer une scrollbar H ou V  ,  à essayer d integrer
from fenetreMultiplesStade import *
from testDoublons import *
from fenetresAides import *
#from creationPoules import *

poules={}
SelectDept=[]
StadeEquipes = {}       ## creation d un dictionnaire pour enregistrer les equipes par stade
listeEquipes =[]        ## pour créer des liste d' équipe par stade

def importDeptSelect(self):
    fileDept = csv.reader(open('DeptSelect.csv', 'r'))
    # listeDept est la liste des departements avec le numéro et la région
    for row in fileDept:
        ##SelectDept.append([row[0], row[1], row[2]])  #ancienne version
        SelectDept.append([row[0], row[1], row[2],0])     ## nouvelle version modif jerome  pour integrer des colonnes vides pour resultats
                                                                    ## À modifier pour adapter en fonction du nombre d'équipe par stade definie au départ'


         

    
class affichagePremierTour(Frame):
    
    def __init__(self):
        Frame.__init__(self)
        
        self.master.geometry("1200x900")
        self.master.config(bg ="white",height=1)
        self.master.title('Répartition stade avec les '+str(len(SelectDept))+' équipes sélectionnées')
        self.master.positionfrom("user") ## placement manuel de la fenetre      
        self.master.sizefrom("user") ## dimensionnement manuel de la fenetre
        
        
        
       
        self.grid(row = 0, column=0, sticky="NSEW")
        self.config(bg="white")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        print("\n PREMIER TOUR \n")
    
        effectifPoule = 4
        importDeptSelect(self)  ## importer le fichier sur lequel on travail
        NbEquipe=int(len(SelectDept)) #calcul le nombre d équipes selectionées
        
        
        
        print("\n CRÉATION DES POULE ET DU DICO STADE \n")
        
        
        orgaPoule= creationPoule1(NbEquipe,effectifPoule)      ## calcul le nombre d'équipe par poule 
                                                    ## et donc la création des poules
        
        print("nombre d'équipe: ",NbEquipe, "\n")
        print("Liste des équipes: ",SelectDept,"\n")
        print("Organisation des poules: ",orgaPoule,"\n")
        
        
        StadeRepartition = creationStade1(orgaPoule, SelectDept)  ## création des poules avec les equipes
                                                ## test pour ne pas avoir de même region dans une poule
        
        print("equipes par stade\n",StadeRepartition)
        
        Stade(self.master, StadeRepartition,NbEquipe)    #lance la procédure stade
        


    
    
def Stade(self, StadeRepartition, nombreEquipes):
    
    stade = StadeRepartition
    NbEquipe = nombreEquipes
   
    ## variables utilisé dans les boucles
    s=0
    k=0
    l=0
    j=0
    
    ligneNumero=1
    colonnePosition=0           #permet de mettre les colonnes en dessous si dépassement du nombre maxi de colonne par ligne
    NbColonneMax=4              # nb de colonne maxi par ligne pour affichage

    listeEquipes =[] 
      
    colonne=4
    
    ## des print sont utilisés pour voir des infos
    print("Nombre de stades: ",len(stade))  ## permet d'afficher le nombre de stade
    print("\n")
    print (" tournois avec la repartition suivante: \n ")
    print (stade)  
   
    
    # affichage des colones pour les stades
    while k < (len(stade)):
        
        ##NumeroStade = ('Stade'+str(k+1))          ## nom et numero du stade
        NumeroStade = (k+1)
                                                ## qui sert de clé dans 
                                                ## le dictionnaire stade indiqué en variable dans la def
                                                
        
        StadeEquipes = stade                    ## StadeEquipes est le dictionnaire
        
        ligne = len(stade[NumeroStade])
        print("NOMBRE D'EQQUIPE SUR LE",NumeroStade,": ",ligne)
        
        
        ####pour le bouton, la command = partial (....) permet de rajouter des variable à la commande
        #### ne pas oublier de faire l'import de functools
        #### si on clique sur le nom du stade qui est un bouton, une autre fenetre s'ouvre avec le nom du stade
        
        nomStade = ("Stade "+str(NumeroStade)) ## permet de mettre un texte devant le numero du stade: variable nomStade
        
        self.bouton1 = Button(self, text=nomStade, command = partial(nouvelle_fenetre, NumeroStade, StadeEquipes), width=30, height=1,bg='#aa0000',fg='white')
        self.bouton1.grid(row=0+ligneNumero, column=colonnePosition,padx =0, pady =0, sticky=NSEW)  # titre de la colonne incrementée de 1 à chaque fois
                                                                                           
        
        while j < ligne and s < NbEquipe:   # le test de s évite les erreurs de dépassement du nombre d équipes'
            ##NumEquipe=X[s]
            
            
            ##textAffichage = (str(Dept[NumEquipe][0])+" "+str(Dept[NumEquipe][2]))
            
            listeEquipes=stade[NumeroStade]  # mettre dans une liste 'equipes'' la liste du dico 'StadeEquipe' qui a la clée 'variable'
            
            textAffichage = (listeEquipes[j][0:3])
            txt1 = Label(self, text = textAffichage, width=30, height=1) 
            
            
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
            
        
 
    ##bouton suivant pour passer à l'étape suivante
    self.bouton2 = Button(self, text='Suivant', command=self.destroy)
    self.bouton2.grid(row = 2, column = 10,  padx =0, pady =0, sticky =NSEW)
    
    ###affiche la fenetre aidePremierTour definie dans le fichier fenetresAides.py 
    self.bouton3 = Button(self, text='Aide', command=aidePremierTour)  
    self.bouton3.grid(row = 1, column = 10,  padx =0, pady =0, sticky =NSEW)


if __name__ == "__main__":
    
    fen2=Tk()
    fen2.config(bg ="blue",height=1)
    
    appli = affichagePremierTour()
    appli.mainloop()
    
   
