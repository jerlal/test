# -*- coding: utf-8 -*-
#!/usr/bin/python3

## en cochant les cases des boutons radio

from tkinter import *
root = Tk()
var = StringVar()
col=0
##valeurResultat = [("victoire",3), ("nul",2), ("défaite",1),("forfait",0),("forfait",3),("défaite",2), ("nul",1),("victoire",0)]
valeurResultat = [(3,"victoire",3), (2,"nul",2), (1,"défaite",1),(1,"victoire",3), (2,"nul",2), (3,"défaite",1)]
#for i in range(8):
    #rad = Radiobutton(root, text=str(i), variable=var, value=str(i % 3))
    #rad.pack(side=LEFT)
    
ligne=0
i=0
for position,text, valeur in valeurResultat:
      
        
    bouton = Radiobutton(root, text=text, variable=var, value=(position%3))
                  
    bouton.grid(row=ligne, column=1+col)
    
    bouton.config(bd=2,fg="black",bg="white")
    
    col+=1
    i+=1
    if i<4:
        col+=1
        i+=1
    else:
        col=0
        i=0
        ligne+=1
    
        

root.mainloop()
