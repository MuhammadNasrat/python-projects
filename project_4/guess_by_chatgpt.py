import random

def show_score(attempts):
    if not attempts:
        print("No old scores, start playing!")
    else:
        print(f"The current high score is {min(attempts)} attempts")

def play_game():
    attempts = []
    random_num = random.randint(1, 10)
    player_name = input("What is your name? ")
    print(f"Hello {player_name}, welcome to the guessing game!")

    wanna_play = input(f"Would you like to play? (yes/no): ").lower()

    if wanna_play == "no":
        print("Ok, maybe next time!")
        return
    else:
        show_score(attempts)

    while wanna_play == "yes":
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                raise ValueError("The number should be within the given range (1-10)")

            attempts.append(guess)
            
            if guess == random_num:
                print("Congratulations! You guessed it right.")
                print(f"It took you {len(attempts)} attempts.")
                wanna_play = input("Do you want to play again? (yes/no): ").lower()
                if wanna_play == "no":
                    print("Thanks for playing! Goodbye.")
                    break
                else:
                    attempts = []
                    random_num = random.randint(1, 10)
                    show_score(attempts)
            else:
                print("Try again!")

        except ValueError as err:
            print(err)

if __name__ == "__main__":
    play_game()
