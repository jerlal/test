# -*- coding: utf-8 -*-
# python version 3.4 
#!/usr/bin/python3
import random 
import csv
import numpy
SelectDept=[]

def importDeptSelect():
    fileDept = csv.reader(open('DeptSelect.csv', 'r'))
    # listeDept est la liste des departements avec le numéro et la région
    for row in fileDept:
        SelectDept.append([row[0], row[1], row[2]])
    
importDeptSelect()
print("nb d'équipe selectionnées:  ",len(SelectDept),"\n")

"""test des fonctions élémentaires du module générateur de nombres pseudo-aléatoires""" 

#X = [('paris',75 ), ('bordeau',1) , ('lyon',2) ,( 'moi',3), ('toi',4) , ('nous',5)] ## ligne pour tester
X = SelectDept


 
 
def ChoixParmi(L):
    """Choisis au hasard un élément dans une séquence""" 
    j=0
    std=1
    
    for i in range(0, int(len(L)/4)): 
        print("Stade :",std)
        
        while j< 4:
            print(random.choice(L))
            j+=1
        j=0
        std+=1
        print(" ")
        
            
    
    ##adaptation Eric
	#i = random.randint(0, len(L) - 1)  
	#elem = L[i]
	
	#nb_elem = len(L) 
	#indices = []  
	
	#while nb_elem > 0:  
		#i = random.randint(0, len(L) -1)  
		#while i in indices: # tant que le tirage redonne un nombre déjà choisi  
			#i = random.randint(0, len(L) -1)  
		#indices.append(i)  
		#nb_elem = nb_elem - 1  
	#resultat = []  
	#for index in indices:
		
		#if L[index][2] not in resultat: # vérifie si la région n'est pas déjà sélectionnée
			##print(SelectDept[index][2]) # affiche bien que les départements non de la même région
			#resultat.append(L[index][2])
            
	#print(resultat) # # affiche bien que les départements non de la même région
	#print(len(resultat))
    
    ## fin adaptation Eric

def ChoixParmiResultat(liste):
    return ChoixParmi(liste)
 
def Battre(L): 
    """Mélanger""" 
    
    random.shuffle(L)
    
    ##permet d'afficher le mélange
    std=1
    j=0
    num=0
    for i in range(0, int(len(L)/4)): 
        print ("stade: ",std)
        while  j<4:
            print(L[num])
            num+=1
            j+=1
        j=0
        std+=1
        print("")
    ## retourne la liste mélangée
    return (L)
    
def BattreTest(L): 
    """Mélanger""" 
    
    random.shuffle(L)
    
    ##test du melange pour eviter des dept de même region sur le même stade
    ##peut-etre que je devrais créer des liste avec le titre du stade au debut de chaque liste de 4 équipes
    
    
    ## ensuite, pour chaque stade,je dois tester si le nom de la region est présent plus d'une fois
    
        ##pour un groupe de 4 équipes, je test si l'argument region est en plusieurs exemplaires:
            ##pour chaque groupe de 4, je trie par ordre alphabétique les regions pour tester plus rapidement
            
    ##si oui alors je supprime la region en double et mets donc une equipe d'une autre région à la place
    ##si non alors je teste le dept suivant
    ##ensuite je passe au stade suivant 
    
    
    
    
    ##permet d'afficher le mélange
    std=1
    j=0
    num=0
    for i in range(0, int(len(L)/4)): 
        print ("stade: ",std)
        while  j<4:
            print(L[num])
            num+=1
            j+=1
        j=0
        std+=1
        print("")
    ## retourne la liste mélangée
    return (L)
def testMelange(liste):
    
    # test si sur un même stade de 4 equipes, il y a des équipes de la même region
    
    
    return
    
    
## recherche avec numpy et array
##  comment fonctionne array
ChoixStade=[]
for i in range(0, len(X)):
     ##premier test avec array
    ChoixStade = numpy.array(X)
    
print("choix stade")
print(ChoixStade)
print("")
##fin de l'utilisation de array


 
def main(): 
    """Fonction principale""" 
    
   
    print("autre melange avec test\n", " à terminer\n")
    ChoixParmiResultat(X)
    print("melange \n")  
    Battre(X) 
    print("melange avec test 1\n")  
    BattreTest(X)
    
    print("\n")
    
   
 
 
if __name__ == '__main__': 
    main() 
