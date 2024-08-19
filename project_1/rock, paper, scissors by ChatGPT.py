import random

def get_computer_play():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_play, computer_play):
    if user_play == computer_play:
        return "It's a tie!"
    elif (user_play == 'rock' and computer_play == 'scissors') or \
         (user_play == 'scissors' and computer_play == 'paper') or \
         (user_play == 'paper' and computer_play == 'rock'):
        return "You win!"
    return "You lose!"

user_name = input("Enter your name: ")
user_play = input("Enter your play (rock, paper, scissors): ").lower()

if user_play in ['rock', 'paper', 'scissors']:
    computer_play = get_computer_play()
    print(f"{user_name} played: {user_play}")
    print(f"Computer played: {computer_play}")
    print(determine_winner(user_play, computer_play))
else:
    print("Invalid play. Please enter rock, paper, or scissors.")
