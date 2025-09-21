import pandas as pd
import os

liste_name_files =  os.listdir(r"\\wsl.localhost\Ubuntu\home\luna\mon_projet\data")   # avoir la liste des fichiers txt
data_dir = r"//wsl.localhost/Ubuntu/home/luna/mon_projet/data/"




"""contenue=[]
for files in liste_name_files:
    monfichier = open(data_dir+str(liste_name_files[2]) , "rt") # ouvrir fichier.txt pour lire le texte
    contenu = monfichier.read() # lire le fichier 
    monfichier.close() # ferme le fichier
    contenu= contenu.split() 
    contenue.append(contenu) #liste imbiquer du contenu de chaque fichier
"""

print(liste_name_files)

#permet de compter le nbr de mot que compose un fichier txt : renvoie une liste par ordre des fichiers traiter

nb_mot=[]
cpt=0
for files in liste_name_files:
    monfichier = open(data_dir+str(liste_name_files[cpt]) , "rt") # ouvrir fichier.txt pour lire le texte
    contenu = monfichier.read() 
    monfichier.close() 
    nb_mot.append(len(contenu.split()))
    cpt+=1




tableau = pd.DataFrame({"files": liste_name_files , "nbr de mots": nb_mot })

print(tableau)
print(tableau["files"])

