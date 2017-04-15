# -*- coding: utf-8 -*-
#!/usr/bin/python3

## regrouper toutes les def qui gèrent les differentes sauvegardes

import os

from tkinter import *
from tkinter.filedialog import *
from tkinter import filedialog

class rechercheFichier(Frame):

    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        #self.parent.title("Résultats ")
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=20)
        self.master.geometry("400x150") #Premier chiffre pour horizontale
        ##self.master.config(bg="white")
         
        self.columnconfigure(0, weight=10)
        self.rowconfigure(0, weight=10)
        self.grid(sticky="NSEW")
        self.config(bg="blue")
        
        
    def rechFichier(self):
        filepath = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
        photo = PhotoImage(file=filepath)
        canvas = Canvas(self, width=photo.width(), height=photo.height(), bg="yellow")
        canvas.create_image(0, 0, anchor=NW, image=photo)
        canvas.grid()

    def choisir_dossier(self):
        "ouvre un dialogue de sélection de répertoire"
        # voir http://tkinter.unpythonic.net/wiki/tkFileDialog
        dossier = filedialog.askdirectory(
            title="Sélectionnez un dossier ",
            mustexist=True,
            parent=self,
        )
        # un dossier a vraiment été sélectionné ?
        if dossier:
            # on remplit la liste de fichiers
            remplir_liste(dossier)
        # end if
    # end def

        
        
            
def rechFichierOK():
    filepath = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
    photo = PhotoImage(file=filepath)
    canvas = Canvas(fenetre, width=photo.width(), height=photo.height(), bg="yellow")
    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.grid()

def choisir_dossierOK():
    "ouvre un dialogue de sélection de répertoire"
    # voir http://tkinter.unpythonic.net/wiki/tkFileDialog
    dossier = filedialog.askdirectory(
        title="Sélectionnez un dossier ",
        mustexist=True,
        parent=fenetre,
    )
    # un dossier a vraiment été sélectionné ?
    if dossier:
        # on remplit la liste de fichiers
        remplir_liste(dossier)
    # end if
# end def


##def updateAttendance():
    ### met à jour la listBox des départements présents
    ##lbDept.delete(0, END)
    ##cr = csv.reader(open("DeptSelect.csv".encode('utf-8'),"rt")) #on récupére le fichier
    ##datalist = list(cr) #on le met sous forme de liste
    ##c = csv.writer(open("DeptSelect.csv".encode('utf-8'), "wt")) #on écrit dans le fichier
    ##for x in range(0, len(listeDept)):
        
        ##if listeDept[x][3].get() == 1:
            ##lbDept.insert(END, listeDept[x][1]+"-"+listeDept[x][0])
            ##c.writerows([[listeDept[x][0],listeDept[x][1],listeDept[x][2]]])

        ###On met writerows (au pluriel) pour pouvoir écrire plusieurs
        ###ligne, on concatène la liste "datalist" avec la
        ###ligne à ajouter (il faut la mettre sous forme d'une liste de liste)


def updateAttendance(nomDuFichier):
    # met à jour la listBox des départements présents
    
    nomFichier = nomDuFichier+".csv"   ##pour avoir un fichier au format csv
    
    lbDept.delete(0, END)  ##permet d'éffacer l'affichage de la liste et de metre la nouvelle liste à la place
    
    cr = csv.reader(open(nomFichier.encode('utf-8'),"rt")) #on récupére le fichier
    datalist = list(cr) #on le met sous forme de liste
    c = csv.writer(open(nomFichier.encode('utf-8'), "wt")) #on écrit dans le fichier
    for x in range(0, len(listeDept)):
        
        if listeDept[x][3].get() == 1:
            lbDept.insert(END, listeDept[x][1]+"-"+listeDept[x][0])
            c.writerows([[listeDept[x][0],listeDept[x][1],listeDept[x][2]]])

        #On met writerows (au pluriel) pour pouvoir écrire plusieurs
        #ligne, on concatène la liste "datalist" avec la
        #ligne à ajouter (il faut la mettre sous forme d'une liste de liste)


## sauvegarde et restitution de dico à ecrire à partir de :

## recupere sur le site 
## http://fsincere.free.fr/isn/python/cours_python_fichier.php

##Un exemple de sauvegarde d'un dictionnaire :

##import pickle

### création d'un dictionnaire
##departement = {36:'Indre',30:'Gard',75:'Paris'}

### enregistrement du dictionnaire dans un fichier
##Fichier = open('data.txt','wb')
##pickle.dump(departement,Fichier)    # sérialisation
##Fichier.close()

##Unpickling

##L'opération inverse est tout aussi simple :

##import pickle

### récupération du dictionnaire
##Fichier = open('data.txt','rb')
##Dept = pickle.load(Fichier)    # désérialisation
##Fichier.close()

##print(Dept)
##print(Dept[36])

##>>>
##{75: 'Paris', 36: 'Indre', 30: 'Gard'}
##Indre

## fin de sauvegarde de dico 

if __name__ =='__main__':
    
    fenetre = Tk() 
    
    rechercheFichier(fenetre)
    rechercheFichier.rechFichier(fenetre)
    rechercheFichier.choisir_dossier()
    rechercheFichier.mainloop()
