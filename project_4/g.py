import random

attempts = []

def showScore():
    if not attempts:
        print("No old scores, Start playing!")
    else:
        print(f"The current high score is {min(attempts)} attempts")

randomNum = random.randint(1, 10)
playerName = input("What is your name? ")

wannaPlay = input(
    f"Hello {playerName}, would you like to play? "
    "enter : yes/no ").lower()

if wannaPlay == "no":
    print("Ok, maybe next time!")
    exit()
else:
    showScore()

while wannaPlay == "yes":
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < 1 or guess > 10:
            raise ValueError("The number should be within the given range")

        attempts.append(1)
        if guess == randomNum:
            print("You guessed it!")
            attempts.append(len(attempts) + 1)
            print(f"It took you {len(attempts)} attempts")
            wannaPlay = input("Do you want to play again? Enter yes/no: ").lower()
            if wannaPlay == "no":
                print("Thanks for playing!")
                break
            else:
                attempts = []
                randomNum = random.randint(1, 10)
                showScore()
        else:
            print("Try again!")

    except ValueError as err:
        print(err)
