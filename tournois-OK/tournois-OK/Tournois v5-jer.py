# -*- coding: utf-8 -*-
#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
#from decimal import Decimal
import random
import csv
from functools import partial ## permet dans un bouton d'avoir une commande avec des variable
import scrollbarJerome  ##programme jerome permettant d'integrer une scrollbar H ou V  ,  à essayer d integrer
from creationPoules import *
from fenetreMultiplesStade import *



  
class Checkbar(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.grid()
        j = 0
        k = 0
        l = (len(listeDept))
        col = 0

        while col < (nbCol+1):
            while j < (nb/nbCol) and k < l:

                nomDept = listeDept[k][0]
                numDept = listeDept[k][1]
                NomRegion = listeDept[k][2]
                listeDept[k][3] = IntVar()
                chkBtn = Checkbutton(
                    self,
                    text=numDept+"-"+nomDept,
                    command=updateAttendance,
                    variable=listeDept[k][3],
                    fg="#000000", bg="#ffffff",
                    activebackground="red")
                chkBtn.grid(row=j+1, column=col+2, padx=10, pady=0, sticky=W)
                k += 1
                j += 1  # permet de placer les textes les uns en dessous des autres. Faire varier la valeur de +4 pour voir l'effet'

            j = 0
            col += 1


def updateAttendance():
    # met à jour la listBox des départements présents
    lbDept.delete(0, END)
    cr = csv.reader(open("DeptSelect.csv".encode('utf-8'),"rt")) #on récupére le fichier
    datalist = list(cr) #on le met sous forme de liste
    c = csv.writer(open("DeptSelect.csv".encode('utf-8'), "wt")) #on écrit dans le fichier
    for x in range(0, len(listeDept)):
        
        if listeDept[x][3].get() == 1:
            lbDept.insert(END, listeDept[x][1]+"-"+listeDept[x][0])
            c.writerows([[listeDept[x][0],listeDept[x][1],listeDept[x][2]]])
    
    
#On met writerows (au pluriel) pour pouvoir écrire plusieurs
#ligne, on concatène la liste "datalist" avec la
#ligne à ajouter (il faut la mettre sous forme d'une liste de liste)

	    
def case_vide(ligne, colonne):
    label = Label(fen, text="").grid(row=ligne, column=colonne)


def importDept():
    fileDept = csv.reader(open('Departements.csv', 'r'))
    # listeDept est la liste des departements avec le numéro et la région
    for row in fileDept:
        listeDept.append([row[0], row[1], row[2], row[3]])


listeDept = []

importDept()

DeptEnr=[]

nb = len(listeDept)     # comptage du nb de departement
nbCol = 5               # nombre de colonne pour affichage
print ("nombre de département au total en France : ",len(listeDept))  # affichage du nombre de departement

if __name__ == '__main__':
    fen = Tk()
    fen.title('liste des '+str(len(listeDept))+' départements')     # titre de la fenetre avec le nombre de département
    fen.geometry("1400x900")
    fen.config(bg="white")
    
    


    tgl = Checkbar(fen)
    tgl.config(relief=GROOVE, bd=0, bg='#ffffff')
    tgl.grid(row=5,  column=0)
    
    lbDept = Listbox(fen)   # crée une listBox des départements présents
    sbDept = Scrollbar(fen, orient=VERTICAL)
    sbDept.config(command=lbDept.yview)
    lbDept.config(yscrollcommand=sbDept.set)
    lbDept.grid(row=5, column=3, sticky=N+S)
    sbDept.grid(row=5, column=3, sticky=N+S+E)
    
    def setAttendance():  # selectionne tous les départements
        for x in range(0, len(listeDept)):
            listeDept[x][3].set(1)
        btnSetAll.config(text='Tout décocher')
        btnSetAll.config(command=unSetAttendance)
        updateAttendance()
	
    def unSetAttendance():  # déselectionne les départements
        for x in range(0, len(listeDept)):
            listeDept[x][3].set(0)
        btnSetAll.config(text='Tout cocher')
        btnSetAll.config(command=setAttendance)
        updateAttendance()
        
    
    
              

    label_info = Label(
        fen,
        text="Cocher les cases pour valider la présence des départements",
        foreground="#000000",
        background="#FFFFFF",
        font="Courier 15 bold italic underline",
        padx="20", pady="4"
        ).grid(row=1, column=0)

    label_dept = Label(fen, text="Départements").grid(row=3, column=0, rowspan=2)
    case_vide(4, 0)
    
    btnQuit = Button(fen, text='Suivant', command=fen.destroy)
    btnQuit.grid(row=21, column=2, padx=0, pady=0, sticky=S)
    btnSetAll = Button(fen, text='Tout cocher', command=setAttendance)
    btnSetAll.grid(row=21, column=0,  padx=0, pady=0, sticky=E)
    #btnEnr = Button(fen, text='Enregistrer', command=Enregistrer)
    #btnEnr.grid(row=21, column=1,  padx=0, pady=0, sticky=E)

    
    fen.mainloop()



SelectDept=[]

def importDeptSelect():
    fileDept = csv.reader(open('DeptSelect.csv', 'r'))
    # listeDept est la liste des departements avec le numéro et la région
    for row in fileDept:
        ##SelectDept.append([row[0], row[1], row[2]])  #ancienne version
        SelectDept.append([row[0], row[1], row[2],0])     ## nouvelle version modif jerome  pour integrer des colonnes vides pour resultats
                                                                    ## À modifier pour adapter en fonction du nombre d'équipe par stade definie au départ'
importDeptSelect()
print("nb d'équipe sélectionnées:", len(SelectDept))


Col=int(((len(SelectDept)/4)+0.9))  # permet de determiner le nombre de colonne 
                                    # le +0.9 permet de rajouter une colonne pour les 1, 2 ou 3 équipes restantes
                                    


print("réparties sur ", Col, "stades")






NbEquipe=int(len(SelectDept)) #calcul le nombre d équipes selectionées
X = [i for i in range(0, NbEquipe)]  # la séquence qui sera battue

Battre(X) 
print(X)   




class Stade:
    def __init__(self, ligne, colonne):
        fen2=Tk()
        fen2.title('Répartition stade avec les '+str(len(SelectDept))+' équipes sélectionnées')
        fen2.geometry("1200x900")
        fen2.config(bg="white")
        
        
        fen2.minsize(400, 300) ## taille minimum de la fenetre
        fen2.maxsize(1200,900) ## taille maximum de la fenetre
        fen2.positionfrom("user") ## placement manuel de la fenetre
        fen2.sizefrom("user") ## dimensionnement manuel de la fenetre
        
        
        Dept=SelectDept
        s=0
        k=0
        l=0
        j=0
        ligneNumero=0
        colonnePosition=0           #permet de mettre les colonnes en dessous si dépassement du nombre maxi de colonne par ligne
        NbColonneMax=4              # nb de colonne maxi par ligne pour affichage
        NbEquipe=len(Dept)    #calcul le nombre d équipes selectionées
        StadeEquipes = {}       ## creation d un dictionnaire pour enregistrer les equipes par stade
        listeEquipes =[]        ## pour créer des liste d' équipe par stade
        
        
        creationPoule(NbEquipe,X,SelectDept)  ## création des poules 
        ##print(StadeEquipes)   ##pour verifier le dico des stades avec les équipes
        
        # affichage des colones pour les stades
        while k < colonne:
            
            NumeroStade = ('Stade'+str(k+1))
            
            ##pour le bouton, la command = partial (....) permet de rajouter des variable à la commande
            ## ne pas oublier de faire l'import de functools
            ## si on clique sur le nom du stade qui est un bouton, une autre fenetre s'ouvre avec le nom du stade
            
            Button(fen2, text=NumeroStade,command=partial(nouvelle_fenetre, NumeroStade, StadeEquipes), width=30, height=1,bg='#aa0000',fg='white').grid(row=0+ligneNumero, column=colonnePosition, sticky=NSEW)  # titre de la colonne incrementée de 1 à chaque fois
                                                                                               
            
            
            while j < ligne and s < NbEquipe:   # le test de s évite les erreurs de dépassement du nombre d équipes'
                NumEquipe=X[s]
                
                
                textAffichage = (str(Dept[NumEquipe][0])+" "+str(Dept[NumEquipe][2]))
                txt1 = Label(fen2, text = textAffichage, width=30, height=1) 
                
                
                txt1.config(relief=GROOVE, bd=2,fg="black",bg="white",font="Courier 8",)
               
                txt1.grid(row=j+1+ligneNumero, column=colonnePosition, sticky=NSEW) ##modif jerome affichage departement
                
                ## creation liste equipe par stade
                listeEquipes.append(Dept[NumEquipe])
                ##fin création liste equipe par stade
                
                           
                
                s+=1
                
                j+=1
            ## creation de dictionnaires pour enregistrer les differents stades
            StadeEquipes[NumeroStade] =  listeEquipes
            ## fin creation dictionnaires
            j=0
            k+=1
            listeEquipes=[]        ##  efface le contenu de listeEquipes à chaque changement de stade
            
            colonnePosition+=1
            if k==NbColonneMax or k==2*NbColonneMax or k==3*NbColonneMax or k==4*NbColonneMax or k==5*NbColonneMax:
                ligneNumero+=6
                colonnePosition=0
                
                
            

        print(StadeEquipes)  ##pour info affichage du dic
       

        Button(fen2, text='Suivant', command=fen2.destroy).grid(row = 50, column = 1,  padx =0, pady =0, sticky =NSEW)
        fen2.mainloop()

 
# départ de l'affichage des listes par stade :
if __name__ == "__main__":
    
    f = Stade(4,Col) # défini le nombre de lignes et de colonnes par stade ! il faut en tout 25 stade !!!!

