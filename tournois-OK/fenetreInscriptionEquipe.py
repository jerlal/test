# -*- coding: utf-8 -*-
#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
#from decimal import Decimal
import random
import csv
from functools import partial ## permet dans un bouton d'avoir une commande avec des variable

from sauvegardesDiverses import *
from premierTour import *
from fenetreMultiplesStade import *
from choixResultatMatch import *  ## pour tester fermeture et ouverture frame

class AutoScrollbar(Scrollbar):
    
    ## gestion des scrollbar
    
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        Scrollbar.set(self, lo, hi)
    def pack(self, **kw):
        raise TclError("cannot use pack with this widget")
    def place(self, **kw):
        raise TclError("cannot use place with this widget")
        
def effaceFrame():
    
    ## partie pour tester la destruction  d'une frame 
    ## et garder la fenetre principale (le canvas avec le scroll) 
    ## pour afficher d'autre chose 
   
        
    fen.destroy()
    
    affichagePremierTour()
    
  
class Checkbar(Frame):
    ## affiche les différents départements avec les cases à cocher pour leurs présences 
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
                    text=numDept+"-"+nomDept+"-"+NomRegion,
                    command=partial(updateAttendance,departementSelection),  ## departementSelection contient le nom du fichier dans lequel est enregistré la liste des département selectionnés
                    variable=listeDept[k][3],
                    fg="blue",
                    activebackground="red")
                chkBtn.grid(row=j+1, column=col+2, padx=10, pady=0, sticky=W)
                k += 1
                j += 1  # permet de placer les textes les uns en dessous des autres. Faire varier la valeur de +4 pour voir l'effet'

            j = 0
            col += 1
       
## la def updateAttendance() est transferée dans le programme sauvegardesDiverses
## qui regroupe toutes les def utilisée pour les suavegardes.

## Elle est mise ici en commentaire car c'était sa place d'origine

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
    
    lbDept.delete(0, END)  ##permet d'éffacer l'affichage de la liste et de mettre la nouvelle liste à la place
    
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
        
 

    
    
def case_vide(self,ligne, colonne):
    ## créer une case que l'on peut placer dans la fenetre pour créer un espace occupé
     
    label = Label(self, text="").grid(row=ligne, column=colonne)


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
    fen.geometry("1200x900+60+40")
    fen.config(bg="white")
    ##fen.minsize(1200, 550) ## taille minimum de la fenetre
    ##fen.maxsize(1200,900) ## taille maximum de la fenetre
    fen.positionfrom("user") ## placement manuel de la fenetre
    fen.sizefrom("user") ## dimensionnement manuel de la fenetre
    
    # canvas extensible
    fen.grid_rowconfigure(0, weight=1)
    fen.grid_columnconfigure(0, weight=1)
 
    
    #######
  
    # creation d'un scroll vertical et horizontal
       
    
    verticaleScrollbar = AutoScrollbar(fen)
    verticaleScrollbar .grid(row=0, column=1, sticky=N+S)
    horizontalScrollbar = AutoScrollbar(fen, orient=HORIZONTAL)
    horizontalScrollbar.grid(row=1, column=0, sticky=E+W)
    
    ##un canevas comme contenant
    canvas = Canvas(fen,
                    yscrollcommand=verticaleScrollbar .set,
                    xscrollcommand=horizontalScrollbar.set)
                    
    
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    canvas.config(bg="white")
    
    verticaleScrollbar .config(command=canvas.yview)
    horizontalScrollbar.config(command=canvas.xview)
    
    
    
    
   
    ##frame est la frame principale
    
    frame = Frame(canvas,bg="white",borderwidth=1)
   
    
       
    # frame 1 contient les nom des departement à cocher
    Frame1 = Frame(frame, bg="white",borderwidth=1)
    Frame1.grid(row=0,column = 0)
   
    
    
    # frame 2 contient la liste de départements choisis
    Frame2 = Frame(frame, bg="white",borderwidth=1)
    Frame2.grid(row=0,column = 1)
    

    # frame 3 contient les boutons
    Frame3 = Frame(frame, bg="white",borderwidth=1)
    Frame3.grid(row=1,column = 0)
    
    departementSelection = "DeptSelect"  ## nom du fichier dans lequel est enregistré la liste des départements selectionnés
    
    tgl = Checkbar(Frame1)
    tgl.config(relief=GROOVE, bd=2)
    tgl.grid(row=5,  column=0)
    
    lbDept = Listbox(Frame2,height =25,width=20)   # crée une listBox des départements présents
    sbDept = Scrollbar(Frame2, orient=VERTICAL)
    sbDept.config(command=lbDept.yview)
    lbDept.config(yscrollcommand=sbDept.set)
    lbDept.grid(row=5, column=3, sticky=N+S)
    sbDept.grid(row=5, column=3, sticky=N+S+E)
    

    def setAttendance():  # selectionne tous les départements
        for x in range(0, len(listeDept)):
            listeDept[x][3].set(1)
        btnSetAll.config(text='Tout décocher')
        btnSetAll.config(command=unSetAttendance)
        
        updateAttendance(departementSelection)
	
    def unSetAttendance():  # déselectionne les départements
        for x in range(0, len(listeDept)):
            listeDept[x][3].set(0)
        btnSetAll.config(text='Tout cocher')
        btnSetAll.config(command=setAttendance)
        
        updateAttendance(departementSelection)
        
    
    
              

    label_info = Label(
        Frame1,
        text="Cocher les cases pour valider la présence des départements",
        foreground="#000000",
        background="#FFFFFF",
        font="Courier 15 bold italic underline",
        padx="20", pady="4"
        ).grid(row=1, column=0)

    label_dept = Label(Frame1, text="Départements").grid(row=2, column=0, rowspan=2)
    ##case_vide(fen,4, 0)
    ##label_deptPresents = Label(Frame1, text=len(datalist)).grid(row=3, column=0, rowspan=2)
    
    ## création des boutons aide, cocher ou décocher tous les départements, suivant
    
    ##affiche la fenetre aideInscription definie dans le fichier fenetresAides.py 
    bouton3 = Button(Frame3, text='Aide', command=PremierTourAide)  
    bouton3.grid(row = 21, column = 0,  padx =0, pady =0, sticky =E)
    
    ## bouton qui permet de  cocher ou décocher tous les département en une seul fois
    btnSetAll = Button(Frame3, text='Tout cocher', command=setAttendance)
    btnSetAll.grid(row=21, column=1,  padx=0, pady=0, sticky=E)
    
    ## bouton qui permet de passer à la fentre suivante (affichage des stades)
    btnQuit = Button(Frame3, text='Suivant', command= effaceFrame)  ## detruire la framme mais garder la fenetre fen
    btnQuit.grid(row=21, column=2, padx=0, pady=0, sticky=S)
    
   
    ############
    ## placer ici la gestion des scroll vertical et horizontal
    canvas.create_window(0, 0, anchor=NW, window=frame)
    
    frame.update_idletasks()
    
    canvas.config(scrollregion=canvas.bbox("all"))
    #############
    
    fen.mainloop()
