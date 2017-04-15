# -*- coding: utf-8 -*-
#!/usr/bin/python3

## regroupe toutes les fenetres aides

from tkinter import *
from functools import partial ## permet dans un bouton d'avoir une commande avec des variable

def textPremierTour():
    texteAide="bonjour"
    return texteAide
    
  
    
    
class aide(Toplevel):
    "Fenêtre satellite contenant l'aide"
    
 
    def __init__(self,   **Arguments):
        Toplevel.__init__(self,   **Arguments)
        
        #self.geometry("300x400")  ## 
        self.transient(self.master)  ## bloque la fenêtre devant
        self.resizable(width =1, height =1)    # => 0 empêche le redimensionnement
        self.title("aide")
               
        msg = Message(self, text = self.texteAide)
        msg.config(fg='black', font=('times', 12, 'italic'), padx=10, pady=10)
        
        msg.pack( )    
        
class PremierTourAide(aide):
    texteAide=("ceci est un texte pour aider à l'utilisation de  la fenêtre du premier tour")  
    

class stadesAide(aide):
    texteAide=("ceci est un texte pour aider à l'utilisation de  la fenêtre d' affichge des stades") 


if __name__ =='__main__':
    
    fenetre = Tk() 
    fenetre.geometry("300x400")
    
    textAide = "il faudra écrire ici les infos \n pour aider à enregistrer les départements"  ## le texte à afficher est contenu dans la def textPourAide 
    bouton3 = Button(fenetre, text='Aide premier tour', command=PremierTourAide)
  
    bouton3.grid(row = 10, column = 10, ipadx=50, padx =0, pady =0, sticky =E)
    bouton4 = Button(fenetre, text='Aide stades', command=stadesAide)
  
    bouton4.grid(row = 20, column = 10, ipadx=50, padx =0, pady =0, sticky =E)
    
    fenetre.mainloop()
