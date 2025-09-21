#Cette class permet d en un premier temps de nettoyer localement les fichier txt des sauts de lignes 
# puis de les lire et traiter chacun d eux pour les stoker dans un dictionnaire simple
# le dictionnaire comprend donc en cles les mots qui compose chaque fichier en evitant les doublons et les valeurs
# reste pour l instand vide 

import os

class ReadFiles:
    def __init__(self):
        self.path = os.path.join(os.getcwd(), "data")
        self.list_txt = os.listdir(self.path)
        self.cpt = 0
        self.compilation_dit_txt = {}
        self.textes_nettoyes = {}

    def nettoyer_txt(self):
        for doc in self.list_txt:
            chemin_fichier = os.path.join(self.path, doc)
            with open(chemin_fichier, "r", encoding="utf-8") as f:
                contenu = f.read()
            contenu = contenu.replace("\n", " ")
            contenu= contenu.lower()
            self.textes_nettoyes[doc] = contenu

    def stocker_mot_dict(self):
        for doc in self.list_txt:
            contenu = self.textes_nettoyes.get(doc, "")
            list_str = contenu.split()
            dict_txt = dict.fromkeys(list_str, None)
            for i in dict_txt.items():
                self.compilation_dit_txt.update({i})
            #self.compilation_dit_txt.append({doc:dict_txt})
            self.cpt += 1
        return self.compilation_dit_txt
        




