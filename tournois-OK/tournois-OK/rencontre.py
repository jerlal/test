#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 



def poule (nbEquipeParPoule):
    ## determine les rencontre des équipes dans les poules
    ## création d'un dictionnaire avec  poule de 4 équipes (clée : premier) ou de 5 équipe (clée: second)
    ## on peut definie au départ les equipes qui se rencontre en modifiant le dico
    cas={'premier':[1,4,2,3,1,3,2,4,1,2,3,4],'second':[2,5,3,4,1,5,2,3,1,4,3,5,1,3,2,4,1,2,4,5]}
    
    
    if nbEquipeParPoule == 4:
        match = cas['premier']          ## si 4 equipes dans la poule alors cette conbimnaison est choisie
        
    else:
        match = cas['second']           ## si 5 equipes dans la poule alors cette conbimnaison est choisie
        
    ##print(match)    
    return(match)                       ## retourne la liste comme valeur
    
 
def matchsDifferents(variable):
    
    ## affiche les differents match en fonction du nombre d équipes dans chaque poule (variable)
    NbMatch= (len(variable))/2
    i=0
    j=0
    while i< NbMatch:
        ##print ("equipe "+str(i)+"\n")
        print ("Équipe "+str(variable[j])+" contre équipe "+str(variable[j+1])+"\n")
        j+=2
        i+=1
        
    
def rencontre(nombreEquipe):
    
    ## créer l'ensemble des matchs en fonction du nombre d'équipe
    ## rencontre dans l'ordre: 1 avec 2, 3 avec 4, ...
    
    nbEquipe = nombreEquipe
    
    i=0
    j=1
    
    
    while j< nbEquipe:
        while i+j < nbEquipe:
            i+=1
            print ("equipe "+str(j)+"\n"+"equipe"+str(j+i)+"\n")
        
        j+=1
        i=0
    
if __name__ == "__main__":
    
    match4=poule(4)
    match5 = poule(5)
    print(match4)
    matchsDifferents(match4)
    print("\n")
    print(match5)
    matchsDifferents(match5)
    print("\n")
    rencontre(4)
