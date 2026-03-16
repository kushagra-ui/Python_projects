import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Type rock/paper/scissors or Q to quit: ").lower()
    
    if user_input == "q":
        print(f"Final Score - You: {user_wins} | Computer: {computer_wins}")
        print("Goodbye!")
        quit()
    
    if user_input not in options:
        print("Invalid input, please type rock, paper or scissors")
        continue

    computer_pick = random.choice(options)
    print("Computer picked", computer_pick + ".")

    if user_input == computer_pick:
        print("It's a tie!")
    elif user_input == "rock" and computer_pick == "scissors":
        print("You win! Rock beats scissors")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win! Scissors beats paper")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You win! Paper beats rock")
        user_wins += 1
    else:
        print("You lose!")
        computer_wins += 1

    print(f"Score - You: {user_wins} | Computer: {computer_wins}")

        