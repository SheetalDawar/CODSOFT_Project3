import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock-Paper-Scissors Game")
        print("1. Rock\n2. Paper\n3. Scissors\n4. Quit")
        user_choice = input("Enter your choice (1-4): ")

        if user_choice == "4":
            print("\nThanks for playing! Final Scores:")
            print(f"You: {user_score}  Computer: {computer_score}")
            break

        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if user_choice in ["1", "2", "3"]:
            user_choice = choices[int(user_choice) - 1]
            print(f"\nYou chose {user_choice}. Computer chose {computer_choice}.")
            result = determine_winner(user_choice, computer_choice)
            print(result)

            if "win" in result:
                user_score += 1
            elif "lose" in result:
                computer_score += 1
        else:
            print("Invalid choice, please enter a number out of 1,2,3 ")

if __name__ == "__main__":
    play_game()

