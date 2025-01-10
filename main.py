# LES FONCTIONS : PROJET QUESTIONNAIRE

def poser_question(question):
    score = 1
    titre= question[0]
    choix = question[1]
    bonne_reponse= question [2]
    nb_choix = len(choix)
    print("QUESTION")
    print( "  " +   titre)
    resultat_rep_correct= False
        
    for i in range(0, nb_choix): 
        print(  f" {i+1}- { choix[i]}")
    reponse_int = demander_reponse_num(1 , nb_choix)
    if choix[reponse_int-1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        score += 1
        resultat_rep_correct= True
    else:
        print("Mauvaise réponse")
    print()
    return resultat_rep_correct

def demander_reponse_num (min , max):
    reponse_str = input(f"Votre réponse ( entre {min} et {max} ) : ")
    try :
        reponse_int = int(reponse_str)
        if    min<=reponse_int <= max : 
            return reponse_int
        print(f"ERREUR : Veuille choisir un nombre entre {min} et {max} ")
               
    except :
            print("ERREUR : Veuille rentrer uniquement de chiffre  ")
    return demander_reponse_num(min , max) 

def lance_questionaire(questionnaire):  
    score = 0
    for question in questionnaire:
        if poser_question(question) :
            score += 1
    print(f"Score final = {score}" )  


# question1 =  ("Quelle est la capitale de la France ?"),("Marseille", "Nice", "Paris", "Nantes"),("Paris")

# question2 =  ("Quelle est la capitale de l'Italie ?"),( "Rome", "Venise", "Pise", "Florence"),("Rome")

# question3 =  ("Quelle est la capitale de la Belgique ?"),( "Anvers", "Bruxelles", "Bruges", "Liége"),("Bruxelles")

questionnaire = (
    ("Quelle est la capitale de la France ?",("Marseille", "Nice", "Paris", "Nantes"),"Paris") ,

    ("Quelle est la capitale de l'Italie ?",( "Rome", "Venise", "Pise", "Florence"),"Rome") ,

    ("Quelle est la capitale de la Belgique ?",( "Anvers", "Bruxelles", "Bruges", "Liége"),"Bruxelles")
)
lance_questionaire(questionnaire)



