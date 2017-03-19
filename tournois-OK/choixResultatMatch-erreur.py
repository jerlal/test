# -*- coding: utf-8 -*-
#!/usr/bin/python3

## on met le resultat du match pour chaque equipe et le programme atribut le nombre de points

from tkinter import *
from functools import partial ## permet dans un bouton d'avoir une commande avec des variable
matchPremierTour={}



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

#def resultatsEquipe1(nom, resultatE1):
    #result1 = resultatE1.get()
    #print(nom, resultatE1.get())
    #varresultatE1.set(result1)
    #return result1 
    
def resultatsEquipe1(nom, resultatE1):
    result1 = eval(resultatE1.get())
    print(nom, result1)
    #resultatE1.set(result1)
    return result1 
    
#def resultatsEquipe2(nom, resultatE2):
    #result2 = resultatE2.get()
    #print(nom, resultatE2.get()) 
    #return result2
    
def resultatsEquipe2(nom, resultatE2):
    
    result2 = eval(resultatE2.get())
    resultatE2.set(str(result2))
    print(nom, result2)
    
    return resultatE2.set(str(result2))    
   
   
def testResultatsEquipe(nomEquipe1, result1, nomEquipe2, result2):
    
    print ("résultats: ",nomEquipe1,result1, nomEquipe2, result2)
    
    if result1 == result2:
        point1=2
        point2=2
    if result1 != result2:
        point1=1000
        point2=2000
    
    ## inscription dans le dico du premier tour
    matchPremierTour[nomEquipe1+"-"+nomEquipe2]=(nomEquipe1, result1, point1, nomEquipe2, result2, point2)
    print(matchPremierTour)
    return   matchPremierTour
    
def choixResultat1(fenetreAffichage, nomEquipe1, nomEquipe2, ligneEquipe1):
    

    varResultatEquipe1 =StringVar(fenetreAffichage)
    varResultatEquipe1.set(0)
    varResultatEquipe2 =StringVar(fenetreAffichage)
    varResultatEquipe2.set(0)
    
    
    global matchPremierTour
    var=0
    col=1
    tailleCaracT = "courier 12"
    ligneEquipe = 1 ## sert à placer le texte de l'équipe1 sur la ligne 1
    
    point1=5
    point2=1
    ligne=0
    i=0
       
    
    ##équipe1
    
    ## position ecriture du nom de l'équipe
    txtResultat1 = Label(fenetreAffichage, text=("resultat de l'"+ nomEquipe1))
    txtResultat1.config(bd=2,fg="black",bg="white",font=tailleCaracT)
    txtResultat1.grid(row = ligneEquipe,column = col,sticky=W)
    
    ##affichage resultat equipe 1
    resultatEquipe1 = Entry(fenetreAffichage,width=5,textvariable = varResultatEquipe1)
    ##resultatEquipe1.bind("<Return>", resultatsEquipe1)
    resultatEquipe1.config(bd=2,fg="black",bg="white",font=tailleCaracT)    
    resultatEquipe1.grid(row= ligneEquipe, column = col+1)
    
    
    
    ##validation des resultat par equipe 1      
    btn1=Button(fenetreAffichage, text="validation resultats", command=partial(resultatsEquipe1, nomEquipe1, varResultatEquipe1))
    btn1.grid(row=ligneEquipe, column=col+3)
    #result1= varResultatEquipe1.get()
    result1 = resultatsEquipe1(nomEquipe1, varResultatEquipe1)
    
    
    ##equipe2
    
    ## position ecriture du nom de l'équipe
    txtResultat2 = Label(fenetreAffichage, text=("resultat de l'"+ nomEquipe2))
    txtResultat2.config(bd=2,fg="black",bg="white",font=tailleCaracT)
    txtResultat2.grid(row = ligneEquipe+1,column = col,sticky=W)
    
    ##affichage resultat equipe 2
    resultatEquipe2 = Entry(fenetreAffichage,width=5,textvariable = varResultatEquipe2)
    resultatEquipe2.config(bd=2,fg="black",bg="white",font=tailleCaracT)    
    resultatEquipe2.grid(row= ligneEquipe+1, column = col+1)
    
    ##validation des resultat par equipe  2     
    btn2=Button(fenetreAffichage, text="validation resultats", command=partial(resultatsEquipe2, nomEquipe2, varResultatEquipe2))
    btn2.grid(row=ligneEquipe+1, column=col+3)
    #result2= varResultatEquipe2.get()
    result2 = resultatsEquipe2(nomEquipe2, varResultatEquipe2)
    
    print ("resultat de l'équipe ",nomEquipe1," : ",result1)
    print ("resultat de l'équipe ",nomEquipe2," : ",result2)
    print (nomEquipe1, result1, nomEquipe2, result2)
    print ("RÉSULTATS: ",nomEquipe1, result1, nomEquipe2, result2)
    
    btn3=Button(fenetreAffichage, text="validation des resultats", command=partial(testResultatsEquipe, nomEquipe1, result1, nomEquipe2, result2))
    btn3.grid(row=ligneEquipe+2, column=col+3)
    
    
    testResultatsEquipe(nomEquipe1,result1, nomEquipe2, result2)
    
    ## inscription dans le dico du premier tour
    #resultRencontre = matchPremierTour[nomEquipe1+"-"+nomEquipe2]=(nomEquipe1,resultatEquipe1.get(),point1,nomEquipe2,resultatEquipe2.get(),point2)
    ##print("E1, resultE1,E2, resultE2: ",nomEquipe1,resultatEquipe1, nomEquipe2, resultatEquipe2)
    
    ##print(resultRencontre)
    
       
    

    
   
         


if __name__ == '__main__':   
    fenetre = Tk()
    fenetre.title("Résultats ")
    fenetre.geometry("600x150") ##Premier chiffre pour horizontale
    fenetre.resizable(width=True, height=True)
    #fenetre.minsize("400x200")
    #fenetre.maxsize("800x250")
    fenetre.config(bg="white")
    fenetre.columnconfigure(0, weight=1)
    fenetre.rowconfigure(0, weight=1)
    ##fenetre.grid(sticky="NSEW")
    
    
    
    
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
    fenetreAffichage = fenetre
    
    choixResultat1(fenetreAffichage,nomEquipe1,nomEquipe2,ligneEquipe1)
    
   
    
   
    
    print("premier tour :",matchPremierTour)
    
    label = Label(fenetre) 
    Button(fenetre, text="Quitter", command=fenetre.destroy).grid(row=10) ##bouton de sortie de la fenetre
    fenetre.mainloop()

