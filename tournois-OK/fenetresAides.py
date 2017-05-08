# -*- coding: utf-8 -*-
#!/usr/bin/python3

## regroupe toutes les fenetres aides

from tkinter import *
from functools import partial ## permet dans un bouton d'avoir une commande avec des variable


    
  
    
    
class aide(Toplevel):
    "Fenêtre satellite contenant l'aide"
    "cette version fonctionne correctement mais n'a pas de scrollbar"
    
 
    def __init__(self, **Arguments):
        Toplevel.__init__(self,   **Arguments)
        
        ##self.geometry("300x400")  ## fixe la dimention de la fenetre mais il faudrait rajouter un scroll
        self.transient(self.master)  ## bloque la fenêtre devant
        self.resizable(width =1, height =1)    # => 0 empêche le redimensionnement
        self.title("aide")
          
        msg = Message(self, text = self.texteAide)
        msg.config(fg='black', bg='white', font=('times', 12, 'italic'), padx=10, pady=10)
        
        msg.pack( )   
        
         
#class aide(Toplevel):
    #"Fenêtre satellite contenant l'aide"
    #"autre version de l'affichage d'une fentre aide mais avec le scrollbar"
    #" probleme dans la gestion de l'affichage avec le scrollbar."
    
    #" A revoir"
 
    #def __init__(self, **Arguments):
        #Toplevel.__init__(self,   **Arguments)
        
        #self.geometry("300x400")  ## 
        #self.transient(self.master)  ## bloque la fenêtre devant
        #self.resizable(width =1, height =1)    # => 0 empêche le redimensionnement
        #self.title("aide")
        ###
        #self.texteAide =Text(self, font ="Times", bg ='ivory', bd =1, width =50, height =15)
        #scroll =Scrollbar(self, bd =1, command =self.texteAide.yview)
        #self.texteAide.configure(yscrollcommand =scroll.set)
        #self.texteAide.pack(side =LEFT, expand =YES, fill =BOTH, padx =2, pady =2)
        #scroll.pack(side =RIGHT, expand =NO, fill =Y, padx =2, pady =2)
        ###       
        ###msg = Message(self, text = self.texteAide)
        ###msg.config(fg='black', bg='white', font=('times', 12, 'italic'), padx=10, pady=10)
        
        ###msg.pack( ) 
        
                   
class PremierTourAide(aide):
    texteAide=("ceci est un texte pour aider à l'utilisation de  la fenêtre du premier tour\n \
                Lorem Ipsum \n \
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. \n \
                Maecenas dignissim eleifend auctor.\n  \
                Nulla vel malesuada nulla.\n  \
                Donec sapien eros, imperdiet sit amet nisi non, vehicula tincidunt eros.\n  \
                Aenean luctus ligula in rutrum efficitur. Proin tristique semper diam quis volutpat.\n  \
                Donec dignissim nunc ante, nec tincidunt ante cursus rutrum. \n \
                Phasellus condimentum ex dolor, eget tempor tortor semper vel. \n \
                Proin consectetur, nisl vel eleifend sodales, massa erat vulputate ligula,\n \
                vitae suscipit justo sapien ac tortor.\n \
                Donec hendrerit imperdiet lorem, et sagittis neque euismod ut.\n \
                Suspendisse in ullamcorper tellus. Curabitur tincidunt ligula in aliquam consectetur.\n \
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. \n \
                Maecenas dignissim eleifend auctor. Nulla vel malesuada nulla.\n  \
                Donec sapien eros, imperdiet sit amet nisi non, vehicula tincidunt eros.\n  \
                Aenean luctus ligula in rutrum efficitur. Proin tristique semper diam quis volutpat.\n  \
                Donec dignissim nunc ante, nec tincidunt ante cursus rutrum. \n \
                Phasellus condimentum ex dolor, eget tempor tortor semper vel. \n \
                Proin consectetur, nisl vel eleifend sodales, massa erat vulputate ligula,\n \
                vitae suscipit justo sapien ac tortor.\n \
                Donec hendrerit imperdiet lorem, et sagittis neque euismod ut.\n \
                Suspendisse in ullamcorper tellus. Curabitur tincidunt ligula in aliquam consectetur.\n ")  
    

class stadesAide(aide):
    texteAide=("ceci est un texte pour aider à l'utilisation de  la fenêtre d' affichge des stades") 


if __name__ =='__main__':
    
    fenetre = Tk() 
    fenetre.geometry("300x400")
    
   
    bouton3 = Button(fenetre, text='Aide premier tour', command=PremierTourAide)
    bouton3.grid(row = 10, column = 10, ipadx=50, padx =0, pady =0, sticky =E)
    
    bouton4 = Button(fenetre, text='Aide stades', command=stadesAide)
    bouton4.grid(row = 20, column = 10, ipadx=50, padx =0, pady =0, sticky =E)
    
    fenetre.mainloop()
