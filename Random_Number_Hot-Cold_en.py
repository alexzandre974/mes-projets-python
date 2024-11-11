import random

"""
The goal of this program is to help the user guess the correct number by guiding them using the words hot and cold
Information:
- Bingo / Hot / warm / Cold
"""

Maximum_number = 1

print("""The goal of the game is to guess the correct number using the "Hot/Cold" information :
      There are 3 levels :
      1) Easy : Numbers 1 to 100. Hot = within 10, Warm = within 20 and Cold for the rest.
      2) Medium : Numbers 1 to 200  and the distance is Hot=20, Warm=40, Cold
      3) Hard : Numbers 1 to  300 and the distance is Hot=30, Warm=60, Cold
      4) Custom  : You can choose the maximum number and the distance for Hot and Warm levels

      """)

Difficulty = int(input("Choose a difficulty (1, 2, 3 or 4): "))
while  Difficulty not in [1, 2, 3, 4]:
    print("Invalid choice, please choose a number between 1 and 3")
    Difficulty = int(input("Choose a difficulty (1, 2, 3 or 4): "))
    
if Difficulty  == 1:
    print("You choose the easy difficulty")
    Hot, Warm, Maximum_number = 10, 20, 100
    
elif Difficulty  == 2:
    print("You choose the medium difficulty")
    Hot, Warm, Maximum_number = 20, 40, 200

elif Difficulty  == 3:
    print("You choose the hard difficulty")
    Hot, Warm, Maximum_number = 30, 60, 300
    
else :
    print("You chose the custom difficulty")
    Maximum_number = int(input("Enter the maximum number: "))
    Hot = int(input("Enter the distance for Hot level: "))
    Warm = int(input("Enter the distance for Warm level: "))

print (f"Maximum number: {Maximum_number}, Hot distance: {Hot}, Warm distance: {Warm}")


def Guess_a_number():
    Guess_a_number = random.randint(1, Maximum_number)
    print("A number has been chosen. Try to guess it!")
    
    #To help me test my program
    print("Number to guess: ", Guess_a_number)

    # print("The goal of the game is to guess a number between 1 and 100 using the Hot-Cold information.")

    User_Number = int(input("Guess a number: ")) 
    
    while Guess_a_number != User_Number and 1 <= User_Number <= Maximum_number:
        if Guess_a_number > User_Number:
            difference = Guess_a_number - User_Number
            if difference <= Hot:
                print("You are hot!")
            elif difference <= Warm:
                print("You are Warm.")
            else:
                print("You are Cold.")
        else:
            difference = User_Number - Guess_a_number
            if difference <= Hot:
                print("You are hot!")
            elif difference <= Warm:
                print("You are Warm.")
            else:
                print("You are Cold.")
    
        User_Number = int(input("Guess a number: "))

    print("Bingo ! You guessed the number.")

Guess_a_number()