# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions
SCORE = 10
def poser_question(question):
    score = 0
    titre= question[0]
    choix = question[1]
    bonne_reponse= question [2]
    nb_choix = len(choix)
    print("QUESTION ")
    print(titre)
        
    for i in range(0, nb_choix): 
        print(  f" {i+1}- { choix[i]}")
    print()

    reponse_str = input(f"Votre réponse (entre 1 et {nb_choix}) : ")
    reponse_int = int(reponse_str)
    if choix[reponse_int-1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")
        
    print()


question1 =  ("Quelle est la capitale de la France ?"),("Marseille", "Nice", "Paris", "Nantes"),("Paris")

question2 =  ("Quelle est la capitale de l'Italie ?"),( "Rome", "Venise", "Pise", "Florence"),("Rome")

poser_question(question1)
poser_question(question2)

# poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
# poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", SCORE)
