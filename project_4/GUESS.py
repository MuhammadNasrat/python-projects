import random

attempts = []

def showScore():
    if not attempts:
        print("No old scores, Start playing!")
    else:
        print(f"the curreng high score is {min(attempts)} attempts")


randomNum = random.randint(1, 10)
playerName = input("What is your name? ")

wannaPlay = input(
    f"Hello {playerName}, would you like to play? "
    "enter : yes/no ").lower()

if wannaPlay == "no" :
    print("ok, maybe next time")
    exit()
else :
    showScore()

while wannaPlay == "yes":
    try:
        guess = int(input("guess a number between 1 and 10 : "))
        if guess < 1 or guess > 10 :
            raise ValueError("the number should be within the given range")
    except ValueError as err:
        print(err)



