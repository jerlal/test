#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## programme récupéré sur le site:
## https://www.developpez.net/forums/d1464319/autres-langages/python-zope/gui/tkinter/tkinter-afficher-liste-fichiers-d-dossier-fenetre/

## permet de choisir un fichier dans un dossier et d'afficher son contenu

import os
import glob
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
 
# zone de définition de fonctions
 
def choisir_dossier ():
    "ouvre un dialogue de sélection de répertoire"
    # voir http://tkinter.unpythonic.net/wiki/tkFileDialog
    dossier = filedialog.askdirectory(
        title="Sélectionnez un dossier de recettes de cuisine",
        mustexist=True,
        parent=fenetre,
    )
    # un dossier a vraiment été sélectionné ?
    if dossier:
        # on remplit la liste de fichiers
        remplir_liste(dossier)
    # end if
# end def
 
def remplir_liste (dossier):
    """
        remplit la liste de fichiers à partir de l'emplacement
        @dossier fourni en paramètre de fonction;
    """
    # init globales
    global dossier_actuel
    # on conserve le dossier en cours de traitement
    dossier_actuel = dossier
    # on récupère la liste des fichiers
    _liste_fichiers = glob.glob(normaliser(dossier, motif_fichiers))
    # on vide d'abord la listbox
    listbox_fichiers.delete(0, END)
    # on remplit via les méthodes de la listbox
    listbox_fichiers.insert(END, *_liste_fichiers)
# end def
 
def normaliser (chemin, *args):
    "met un chemin de fichier en conformité avec l'OS utilisé"
    return os.path.normpath(os.path.join(chemin, *args))
# end def
 
def afficher_fichier (event):
    "affiche le contenu du fichier sélectionné"
    # on récupère le nom du fichier
    fichier = normaliser(
        dossier_actuel,
        listbox_fichiers.get(listbox_fichiers.curselection() or 0)
    )
    # est-ce réellement un fichier ?
    if os.path.isfile(fichier):
        # oui, on peut l'ouvrir
        with open(fichier) as file_in:
            # on efface d'abord la zone de texte
            affichage_texte.delete("1.0", END)
            # on insère le nouveau contenu texte du fichier
            affichage_texte.insert("1.0", file_in.read())
        # end with
    # end if
# end def
 
# début du programme
 
# init variables globales
dossier_actuel = ""
motif_fichiers = "*.txt"
 
# on commence par établir l'interface graphique (GUI)
# on crée la fenêtre principale
fenetre = Tk()
fenetre.title("Mon livre de recettes")
# SVP, NE FORCEZ PAS LA GÉOMÉTRIE de la fenêtre /!\
# elle va s'adapter toute seule...
#~ fenetre.geometry("1000x800") --> c'est NON !
# d'autant plus qu'elle sera REDIMENSIONNABLE ensuite
# on ajoute des composants graphiques à la fenêtre principale
# on crée un conteneur pour la gestion des fichiers
conteneur_fichiers = Frame(fenetre)
# on rend le conteneur redimensionnable
conteneur_fichiers.columnconfigure(0, weight=1)
conteneur_fichiers.rowconfigure(1, weight=1)
# on crée une étiquette texte dans ce conteneur
Label(
    conteneur_fichiers,
    text="Veuillez sélectionner un fichier :"
).grid(row=0, column=0, sticky=EW)
# on crée la liste des fichiers
#~ cvar_fichiers = StringVar() # devenu INUTILE (vous pouvez supprimer)
#~ listbox_fichiers = Listbox(conteneur_fichiers, listvariable=cvar_fichiers) # IDEM ici (à supprimer)
 
# ATTENTION: le NOM de la globale a été CHANGÉ
# de 'liste_fichiers' à 'listbox_fichiers' /!\
# tenez-en compte lors de la mise à jour de vos propres scripts /!\
listbox_fichiers = Listbox(conteneur_fichiers)
listbox_fichiers.grid(row=1, column=0, sticky=NS+EW)
 
# avec sa scrollbar
vbar_fichiers = Scrollbar(conteneur_fichiers, orient=VERTICAL)
vbar_fichiers.grid(row=1, column=1, sticky=NS+W)
# on connecte la scrollbar à la liste des fichiers
listbox_fichiers.configure(yscrollcommand=vbar_fichiers.set)
vbar_fichiers.configure(command=listbox_fichiers.yview)
# on va gérer l'affichage des recettes sur simple clic
# sur un fichier de la liste
listbox_fichiers.bind("<ButtonRelease-1>", afficher_fichier)
# on crée un bouton de type 'Parcourir'
Button(
    conteneur_fichiers,
    text="Sélectionner un dossier",
    command=choisir_dossier,
).grid(row=2, column=0)
# on place le conteneur dans la fenêtre principale
# avec des marges padx et pady
conteneur_fichiers.grid(row=0, column=0, sticky=NS+EW, padx=5, pady=5)
# on crée un conteneur pour l'affichage
conteneur_affichage = Frame(fenetre)
# on rend le conteneur redimensionnable
conteneur_affichage.columnconfigure(0, weight=1)
conteneur_affichage.rowconfigure(1, weight=1)
# on crée une étiquette texte dans ce conteneur
Label(
    conteneur_affichage,
    text="Recette du jour :"
).grid(row=0, column=0, sticky=EW)
# on crée la zone d'affichage de texte
affichage_texte = ScrolledText(
    conteneur_affichage,
    bg="white",
    fg="blue",
    font="sans 12 bold",
    height=10,
    width=20,
)
affichage_texte.grid(row=1, column=0, sticky=NS+EW)
# on ajoute un bouton 'quitter'
Button(
    conteneur_affichage,
    text="Quitter",
    command=fenetre.destroy
).grid(row=2, column=0, sticky=E)
# on place le conteneur dans la fenêtre principale
# avec des marges padx et pady
conteneur_affichage.grid(row=0, column=1, sticky=NS+EW, padx=5, pady=5)
# on rend la fenêtre redimensionnable
fenetre.rowconfigure(0, weight=1)
fenetre.columnconfigure(1, weight=1)
 
# pour démarrer avec un dossier par défaut,
# ajoutez simplement ceci :
# je veux...
##remplir_liste(r"C:\Python34\Scripts\Recettes")
# test débogage tarball69 ne pas enlever - merci
remplir_liste("./")

 
# pour finir
# on lance la boucle événementielle principale
fenetre.mainloop()
