chaine = str(input("Entrer votre phrase: "))
chaine = chaine.lower()
chaine = chaine.replace("'", " ")

def count_word():

    print(len(chaine.split(" ")))

count_word()