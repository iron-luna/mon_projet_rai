import json

class ModifyFilesJson:

    


    def delete_a_element (self):
        ask= True
        while ask == True:
            with open ("words_translated.json","r", encoding="utf-8") as f:
                contenu = json.load(f)
            user = (input ("Saisir le mot à supprimer: "))
            user=user.lower()
            try:
                del contenu[user]
                with open("words_translated.json", "w", encoding="utf-8") as f:
                    json.dump(contenu, f, ensure_ascii=False, indent=4)
                print("operation reussie")
            except:
                print("Erreur : le mot saisie n' est pas dans la base de donné")
            ask= input("Voulez vous supprimer un autre elemnt? Repondez par oui ou non " )
            ask=ask.lower()
            if ask == "oui" :
                ask = True
            else:
                ask=False


        