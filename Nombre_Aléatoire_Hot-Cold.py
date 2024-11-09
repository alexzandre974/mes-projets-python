import random

"""
Le but de ce programe est que l'utilisateur puise deviner un nombre grace au
informatation du jeux Chaud - Frois
Information :
    - Bingo = trouver
    - chaud = 10
    - neutre = 20
    - froid = reste
"""

def Deviner_un_nombre():
    Nombre_a_deviner = random.randint(1, 100)
    print("nombre a deviner :", Nombre_a_deviner)
    print("Le but du jeux est de deviner un nombre entre 1 et 100 grace au information Chaud-Froid")

    Nombre_utilisateur = int(input("Devinez un nombre : ")) 
    
    while Nombre_a_deviner != Nombre_utilisateur and 1 <= Nombre_utilisateur <= 100:
        if Nombre_a_deviner > Nombre_utilisateur:
            difference = Nombre_a_deviner - Nombre_utilisateur
            if difference <= 10:
                print("Vous êtes chaud !")
            elif difference <= 20:
                print("Vous êtes neutre.")
            else:
                print("Vous êtes froid.")
        else:
            difference = Nombre_utilisateur - Nombre_a_deviner
            if difference <= 10:
                print("Vous êtes chaud !")
            elif difference <= 20:
                print("Vous êtes neutre.")
            else:
                print("Vous êtes froid.")
    
        Nombre_utilisateur = int(input("Devinez un nombre: "))

    print("Félicitations ! Vous avez deviné le nombre.")

Deviner_un_nombre()