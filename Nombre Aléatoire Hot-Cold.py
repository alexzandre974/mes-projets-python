import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Devinez un nombre entre 1 et 100!")

    while not guessed:
        user_guess = int(input("Entrez votre devinette: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Trop bas! Essayez encore.")
        elif user_guess > number_to_guess:
            print("Trop haut! Essayez encore.")
        else:
            guessed = True
            print(f"Félicitations! Vous avez deviné le nombre {number_to_guess} en {attempts} tentatives.")

guess_the_number()