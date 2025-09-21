from utils.read_files import ReadFiles
from utils.input_data_of_key import input_traduction_of_word_by_user
from utils.input_data_of_key import store_json_data
from utils.modify_files_json import ModifyFilesJson

read = ReadFiles ()  
read.nettoyer_txt()    # nettoie les fichiers txt
read.stocker_mot_dict()  # stoke sous forme de dict les mots des fichiers(clés= mots , valeur= None)
compilation_dict_txt = read.stocker_mot_dict()


order="first" 

while order != "" :
    order= input ("""
                    Voulez-vous entrez la traduction des mots inconnue pour le systeme ? Entrer traduire
                  
                    Voulez-vous effacer un element de la liste des mots traduit? Entrer effacer
                  
                    Voulez-vous explorer la liste des mots traduit ? Entrer explorer 
                  
                    Sinon entrer
                    """)
    order=order.lower()

    if order == "traduction":
        input_traduction_of_word_by_user(compilation_dict_txt)   # demande à l' user la traduction des mots(remplie les valeur des clés)
        store_json_data(compilation_dict_txt)                     # stoke les donnés data-valeur dans un fichier json
        

    elif order == "effacer":
        contenu= ModifyFilesJson()
        contenu.delete_a_element()

    elif order == "explorer":
        with open("words_translated.json", "r", encoding="utf-8") as f:
            contenu = f.read()
        print(contenu)
    
    
