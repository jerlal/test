# -*- coding: utf-8 -*-
#!/usr/bin/python3

## pour tester l'affichage et la fermeture de fenetrres
## garde le scroll bar en bas et à droite

from tkinter import *
from functools import partial ## permet dans un bouton d'avoir une commande avec des variable
from premierTour import *


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
        
class enregistrementEquipe(Frame):
    
    ## affiche la frame avec les enregistreme des equipes
    
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.grid()
        
        # frame 1 contient les nom des departement à cocher
        Frame1 = Frame(frame, bg="white",borderwidth=1,height=35)
        Frame1.grid(row=0,column = 0)
        Frame1.rowconfigure(0, weight=100)
        Frame1.columnconfigure(0, weight=100)
        
        
        # frame 2 contient la liste de départements choisis
        Frame2 = Frame(frame, bg="white",borderwidth=1)
        Frame2.grid(row=0,column = 1)
        Frame2.rowconfigure(0, weight=100)
        Frame2.columnconfigure(0, weight=100)
    
        # frame 3 contient les boutons
        Frame3 = Frame(frame, bg="white",borderwidth=1)
        Frame3.grid(row=1,column = 0)
        Frame3.rowconfigure(0, weight=100)
        Frame3.columnconfigure(0, weight=100)
    
        label_info = Label(
            Frame1,
            text="Cocher les cases pour valider la présence des départements",
            foreground="#000000",
            background="#FFFFFF",
            font="Courier 15 bold italic underline",
            padx="20", pady="4"
            ).grid(row=1, column=0)
    
        label_dept = Label(Frame1, text="frame1").grid(row=3, column=0, rowspan=2)
        label_frame2 = Label(Frame2, text="frame2").grid(row=3, column=0, rowspan=2)
        
        
        ##btnQuit = Button(Frame3, text='Suivant', command= partial(pageSuivante,frame)) ## ne fonctionne pas
        btnQuit = Button(Frame3, text='Suivant', command= fenetre2)  ## permet de basculler sur la fenetre suivante
        btnQuit.grid(row=21, column=2, padx=0, pady=0, sticky=S)

class fenetre2(Frame):
    ## affiche une autre frame pour tester
    
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.grid()
        
        # frame 4 contient les nom des departement à cocher
        Frame4 = Frame(canvas, bg="white",borderwidth=1,height=35)
        
        Frame4.grid(row=0,column = 0)
        Frame4.rowconfigure(0, weight=100)
        Frame4.columnconfigure(0, weight=100)
        
        label_info = Label(
            Frame4,
            text="fenetre numero 2 pour test",
            foreground="#000000",
            background="#FF0000",
            font="Courier 15 bold italic underline",
            padx="20", pady="4"
            ).grid(row=1, column=0)
        btnQuit = Button(Frame4, text='Suivant', command= fenetre3)  ## permet de basculler sur la fenetre suivante
        btnQuit.grid(row=21, column=2, padx=0, pady=0, sticky=S)

class fenetre3(Frame):
    ## affiche une autre frame pour tester
    
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.grid()
        
        # frame 1 contient les nom des departement à cocher
        Frame5 = Frame(canvas, bg="white",borderwidth=1,height=35)
        
        Frame5.grid(row=0,column = 0)
        Frame5.rowconfigure(0, weight=100)
        Frame5.columnconfigure(0, weight=100)
        
        label_info = Label(
            Frame4,
            text="fenetre numero 2 pour test",
            foreground="#000000",
            background="#00ff00",
            font="Courier 15 bold italic underline",
            padx="20", pady="4"
            ).grid(row=1, column=0)
        btnQuit = Button(Frame4, text='Suivant', command= fenetre2)  ## permet de basculler sur la fenetre suivante
        btnQuit.grid(row=21, column=2, padx=0, pady=0, sticky=S)
       
        
def pageSuivante(self):
    ##destruction fenetre secondaire
    ## ne fonctionne pas dans l'état'
    return(self.destroy)
    
    
if __name__ == '__main__':
    fen = Tk()
    fen.title('titre de la fenêtre')     # titre de la fenetre avec le nombre de département
    fen.geometry("1200x900+60+40")
    fen.config(bg="white")
    ##fen.minsize(1200, 550) ## taille minimum de la fenetre
    ##fen.maxsize(1200,900) ## taille maximum de la fenetre
    fen.positionfrom("user") ## placement manuel de la fenetre
    fen.sizefrom("user") ## dimensionnement manuel de la fenetre
    
 
    
    #######
  
    # creation d'un scroll vertical et horizontal
       
    
    verticaleScrollbar = AutoScrollbar(fen)
    verticaleScrollbar .grid(row=0, column=1, sticky=N+S)
    horizontalScrollbar = AutoScrollbar(fen, orient=HORIZONTAL)
    horizontalScrollbar.grid(row=1, column=0, sticky=E+W)
    
    canvas = Canvas(fen,
                    yscrollcommand=verticaleScrollbar .set,
                    xscrollcommand=horizontalScrollbar.set)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    canvas.config(bg="white",borderwidth=1)
    
    verticaleScrollbar .config(command=canvas.yview)
    horizontalScrollbar.config(command=canvas.xview)
    
    # canvas extensible
    fen.grid_rowconfigure(0, weight=1)
    fen.grid_columnconfigure(0, weight=1)
    
    #
    ##un canevas comme contenant
    ##frame est la frame pricipale
    
    frame = Frame(canvas,bg="white",borderwidth=1)
    frame.rowconfigure(1, weight=1)
    frame.columnconfigure(1, weight=1)
    
    ################
    
    enregistrementEquipe(frame) ##affiche la frame avec l'enregistrement des equipes
    #fenetre2(frame)     ##affichage d'une seconde fenetre à la place de la première
    
    
    
    ############
    ## placer ici la gestion des scroll vertical et horizontal
    canvas.create_window(0, 0, anchor=NW, window=frame)
    
    frame.update_idletasks()
    
    canvas.config(scrollregion=canvas.bbox("all"))
    #############
    
    fen.mainloop()

