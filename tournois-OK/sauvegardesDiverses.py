# -*- coding: utf-8 -*-
#!/usr/bin/python3

## regrouper toutes les def qui gèrent les differentes sauvegardes


##def updateAttendance():
    ### met à jour la listBox des départements présents
    ##lbDept.delete(0, END)
    ##cr = csv.reader(open("DeptSelect.csv".encode('utf-8'),"rt")) #on récupére le fichier
    ##datalist = list(cr) #on le met sous forme de liste
    ##c = csv.writer(open("DeptSelect.csv".encode('utf-8'), "wt")) #on écrit dans le fichier
    ##for x in range(0, len(listeDept)):
        
        ##if listeDept[x][3].get() == 1:
            ##lbDept.insert(END, listeDept[x][1]+"-"+listeDept[x][0])
            ##c.writerows([[listeDept[x][0],listeDept[x][1],listeDept[x][2]]])

        ###On met writerows (au pluriel) pour pouvoir écrire plusieurs
        ###ligne, on concatène la liste "datalist" avec la
        ###ligne à ajouter (il faut la mettre sous forme d'une liste de liste)


def updateAttendance(nomFichier):
    # met à jour la listBox des départements présents
    lbDept.delete(0, END)
    cr = csv.reader(open("nomFichier.csv".encode('utf-8'),"rt")) #on récupére le fichier
    datalist = list(cr) #on le met sous forme de liste
    c = csv.writer(open("nomFichier.csv".encode('utf-8'), "wt")) #on écrit dans le fichier
    for x in range(0, len(listeDept)):
        
        if listeDept[x][3].get() == 1:
            lbDept.insert(END, listeDept[x][1]+"-"+listeDept[x][0])
            c.writerows([[listeDept[x][0],listeDept[x][1],listeDept[x][2]]])

        #On met writerows (au pluriel) pour pouvoir écrire plusieurs
        #ligne, on concatène la liste "datalist" avec la
        #ligne à ajouter (il faut la mettre sous forme d'une liste de liste)
