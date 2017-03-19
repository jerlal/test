# -*- coding: utf-8 -*-
#!/usr/bin/python3

## en cochant les cases des boutons radio, on choisit le  resultat de l'équipe

from tkinter import *
from functools import partial ## permet dans un bouton d'avoir une commande avec des variable


def sel(numEquipe,ligneEquipe):
    
    
    
    resultat = var.get()
    ##pour mettre ou pas un s à point
    
    if resultat == 2 or resultat == 3:
        point=" points "
    else:
        point=" point  "
        
    selection = ("\n"+numEquipe+ " vous marquez " + str(resultat)+ point)
    
       
    txt = Label(fenetre,text = selection)
    txt.config(bd=2,fg="black",bg="white",font=tailleCaracT)
    txt.grid(row = ligneEquipe+1,column = 0,sticky=W, columnspan=4)
    
 
      
def choixResultat1(nomEquipe1, nomEquipe2, ligneEquipe1):
    var = StringVar()
    col=1
    ligneEquipe = ligneEquipe1
    valeurResultat = [(3,"victoire",3), (2,"nul",2), (1,"défaite",1),(1,"victoire",3), (2,"nul",2), (3,"défaite",1)]
            
    ligne=0
    i=0
    
    for equipeNom in [nomEquipe1,nomEquipe2]:
        
        ## position ecriture du nom de l'équipe
        txtResultat = Label(fenetre, text=("resultat de l'"+ equipeNom))
        txtResultat.config(bd=2,fg="black",bg="white",font=tailleCaracT)
        txtResultat.grid(row = ligneEquipe,column = col,sticky=W)
        
        ##affichage resultat equipe 1
        resultatEquipe1 = Entry(fenetre,width=5)
        resultatEquipe1.config(bd=2,fg="black",bg="white",font=tailleCaracT)    
        resultatEquipe1.grid(row= ligneEquipe, column = col+1)
        
        ##bouton forfaitequipe1
        varEquipe = IntVar()
        boutonForfait= Checkbutton(fenetre, text='forfait', variable=varEquipe)
        boutonForfait.config(bd=2,fg="black",bg="white",font=tailleCaracT)
        boutonForfait.grid(row = ligneEquipe, column = (col+2),sticky=W)
    
        ligneEquipe +=1
        
    
    
   
    for position,text, valeur in valeurResultat:
          
         
          
        bouton = Radiobutton(fenetre, text=text, variable=var, value=(position%3))
                      
        bouton.grid(row=ligne+ligneEquipe1, column=3+col)
        
        bouton.config(bd=2,fg="black",bg="white")
        
        col+=1
        i+=1
        if i<4:
            col+=1
            i+=1
        else:
            col=1
            i=0
            ligne+=1       


if __name__ == '__main__':   
    fenetre = Tk()
    fenetre.title("Résultats ")
    fenetre.geometry("800x100") ##Premier chiffre pour horizontale
    fenetre.resizable(width=True, height=True)
    #fenetre.minsize("400x200")
    #fenetre.maxsize("800x250")
    fenetre.config(bg="white")
    tailleCaracT = "courier 12"
    #var = IntVar()
    
    ## affichage titre
    txt = Label(fenetre,text = "résultats de la rencontre")
    txt.config(bd=2,fg="black",bg="white",font=tailleCaracT)
    txt.grid(row = 0,column = 0,sticky=W, columnspan=4)
    
    
    
    ##affichage équipe 
    ligneEquipe1 = 2  ##utilisé pour positionner dans la fenetre
    nomEquipe1 = "equipe 1"
    nomEquipe2 = "equipe 2"
    
    choixResultat1(nomEquipe1,nomEquipe2,ligneEquipe1)
    
    
    
    label = Label(fenetre) 
      
    fenetre.mainloop()

