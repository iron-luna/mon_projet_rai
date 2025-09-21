import json 

#cette fonction permet de rentrer manuellement les valeur des clés (=la traduction des mots recuperer des fichier txt
# et stoker dans le dictionaire simple compilation_dict_txt) 
#Donc elle demande à l utilisateur de rentrer la traduction
#si la clés et donc le mot existe deja dans le fichier words_translated alors on ne le traite pas (pas besoin de donner
#la traduction d un mot deja donné)

def input_traduction_of_word_by_user(compilation_dict_txt):             
    with open("words_translated.json", "r", encoding="utf-8") as f:
        dict_json = json.load(f)

    for key, value in compilation_dict_txt.items():
        if not key in dict_json:
            print("Traduisez le mot suivant: ")
            input_user = input(str(key) + ": ")
            compilation_dict_txt[key]= input_user
        
        
    return compilation_dict_txt 

#Cette fonction permet de stoker les valeur rentrer par l user dans un fichier json

def store_json_data(compilation_dict_txt):
    compilation_json_format= json.dumps(compilation_dict_txt)
    with open("words_translated.json", "w", encoding="utf-8") as f:
        f.write(compilation_json_format)
    return compilation_json_format




