# -*- coding: utf-8 -*-
#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
#from decimal import Decimal
import random
import csv
from functools import partial ## permet dans un bouton d'avoir une commande avec des variable
import scrollbarJerome  ##programme jerome permettant d'integrer une scrollbar H ou V  ,  à essayer d integrer
from premierTour import *
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
                    fg="blue",
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
    tgl.config(relief=GROOVE, bd=2)
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
   

    
    fen.mainloop()
