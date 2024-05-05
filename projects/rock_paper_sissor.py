import random
def game():
    while True:
        user_input = input("Enter a choice (rock, paper, scissors): ")
        possible_inputs = ["rock","paper","scissors"]
        computer_input = random.choice(possible_inputs)
        print(f"\nyou choose {user_input} and computer choose {computer_input}")
        if user_input == computer_input:
            print("Both of you have selected the same.")
            print("\nSo, It's a tie.")
        elif user_input == "rock":
            if computer_input == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose!")
        elif user_input == "paper":
            if computer_input == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose!")
        elif user_input == "scissor":
            if computer_input == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissor! you lose!")
        
        play_again = input("Do you wish to play again? (yes/no)\n")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    game()
