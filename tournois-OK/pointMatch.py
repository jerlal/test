# -*- coding: utf-8 -*-
#!/usr/bin/python3

## differentes formes de bouton

from tkinter import *
fenetre=Tk()


## pour equipe 1
#value1 = IntVar(fenetre)
value1 = 0
scale1 = Scale(fenetre, from_=0, to=3, showvalue=True, label=' Équipe 1',
variable=value1, tickinterval=1, orient='h')
entry1 = Entry(fenetre, textvariable=value1)

scale1.grid(row=0, column=0)
entry1.grid(row=0, column=1)


## pour equipe 2

#value2 = IntVar(fenetre)

value2 = 3 - value1
print(value2)
texte =("equipe 2: ",value2)
resultat2 =Label(fenetre,text=texte)
resultat2.grid(row=2, column=0)





 
echelles = (
    ('equipe A',0,3,0),
    ('equipe B',0,3,0),
    ('equipe C', 0,3,0),
    ('equipe D',0,3,0),
    
    )
 
for x, (nom, to, from_, _) in enumerate(echelles):
    btn = Button(text=nom)
    scale = Scale(label=nom, from_=from_, to=to, orient=HORIZONTAL)
    btn['command'] = lambda nom=nom, scale=scale: etape_suivante(nom, scale)
    btn.grid(row=4+x, column=0)
    scale.grid(row=4+x, column=1)
 
def etape_suivante(nom, scale):
    print((nom, scale.get()))
    
    
    
vars = list()
colonne =0
for item in ['foo', 'bar', 'stuff']:
        
    var = IntVar()
    Checkbutton(fenetre, text=item,
        variable=var).grid(row=20, column=colonne)
    vars.append(var)
    colonne+=1
    

def state():
    for v in vars:
        print (v.get())

b = Button(fenetre, text='State', command=state)
b.grid(row=21, column=0)    
 
 
fenetre.mainloop()
 



