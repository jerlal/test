# -*- coding: utf-8 -*-
#!/usr/bin/python3

##recupéré sur le site:
## http://python.jpvweb.com/mesrecettespython/doku.php?id=apropos
## et adapté en python3
 
import tkinter
import tkinter.font
 
class Apropos(tkinter.Toplevel):
 
    def __init__(self, master=None):
        tkinter.Toplevel.__init__(self, master)
        self.title("A propos")
        self.mes="""
VotreApplication version 1.40
 
Copyright 2008 VotreNom
Distribution avec license GPL v3
Site http://xxxxxx..com
            """
        police=tkinter.font.Font(self, size=12, family='Arial')
        self.L=tkinter.Label(self, text=self.mes, bg='yellow', font=police).grid()


## Comme c'est du “Toplevel”, cette fenêtre est appelée à l'intérieur d'une application Tkinter, par exemple par un menu qui appelle la méthode suivante: 


#def apropos(self,event=None):
        #"""affiche la fenêtre 'A propos' """
        #self.apr=Apropos()
        #self.apr.focus_set()
