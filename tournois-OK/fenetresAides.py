# -*- coding: utf-8 -*-
#!/usr/bin/python3

## regroupe toutes les fenetres aides

from tkinter import *

def textPremierTour():
    texteAide="bonjour"
    return texteAide
    


class aidePremierTour(Toplevel):
    "Fenêtre satellite contenant l'aide"
    
 
    def __init__(self,   **Arguments):
        Toplevel.__init__(self,   **Arguments)
        
        #self.geometry("300x400")  ## 
        self.transient(self.master)  ## bloque la fenêtre devant
        self.resizable(width =1, height =1)    # => empêche le redimensionnement
        self.title("aide")
        textAide = "il faudra écrire ici les infos \n pour utiliser cette fenetre"  ## le texte à afficher est contenu dans la def textPourAide 
              
          
        msg = Message(self, text = textPremierTour())
        msg.config(fg='black', font=('times', 12, 'italic'), padx=10, pady=10)
        
        msg.pack( )
        
class aideInscription(Toplevel):
    "Fenêtre satellite contenant l'aide"
    
 
    def __init__(self,   **Arguments):
        Toplevel.__init__(self,   **Arguments)
        
        #self.geometry("300x400")
        self.transient(self.master)
        #self.resizable(width =0, height =0)    # => empêche le redimensionnement
        self.title("aide")
        textAide = "il faudra écrire ici les infos \n pour aider à enregistrer les départements"  ## le texte à afficher est contenu dans la def textPourAide 
              
          
        msg = Message(self, text = textAide)
        msg.config(fg='black', font=('times', 12, 'italic'), padx=10, pady=10)
        msg.pack( )


if __name__ =='__main__':
    
    fenetre = Tk() 
    fenetre.geometry("300x400")
    
    
    bouton3 = Button(fenetre, text='Aide', command=aidePremierTour)  
    bouton3.grid(row = 10, column = 10, ipadx=50, padx =0, pady =0, sticky =E)
    
    fenetre.mainloop()
