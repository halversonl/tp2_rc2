import random


def jeu():
   """
    Contient le jeu en entier afin de rendre très facile de le boucler.
   :return:
   """

    # Choix de bornes
    print("Choissisez la borne minimale et la borne maximale pour le jeu.")

    borne_minimale = int(input("Quel est votre borne minimale?: "))
    borne_maximale = int(input("Quel est votre borne maximale?: "))

    if borne_maximale < borne_minimale:
        print("Vu que la borne minimale était plus grande que la borne maximale, on les a échangés.")
        borne_maximale, borne_minimale = borne_minimale, borne_maximale

    # Generation des variables
    nombre = random.randint(borne_minimale,borne_maximale)
    nb_essais = 0
    essai = -1

    # Début du jeu
    print("J’ai choisi un nombre au hasard entre {} et {}. À vous de le deviner...".format(borne_minimale, borne_maximale))
    # print(nombre)
    while essai != nombre:
        essai = int(input("Entrer votre essai: "))
        nb_essais = nb_essais + 1

        # Mauvaises réponses
        if essai > nombre:
            print("Mauvais choix, le nombre est plus petit que {}.".format(essai))
        elif essai < nombre:
            print("Mauvaise réponse, le nombre est plus grand que {}.".format(essai))
    # Bonne réponse
    if essai == nombre:
        print("Bravo! Bonne réponse! Vous l'avez eu en {} essais.".format(nb_essais))

    # Rejouer ou non
    rejouer = input("Voulez-vous faire une autre partie (o/n)?")
    if rejouer == "o":
        jeu()
    elif rejouer == "n":
        print("Merci et au revoir…")


jeu()
