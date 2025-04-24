import random

ROUNDS = 5


def get_guess(): 
    while True:
        guess = input("Enter a number: ")
        if guess.isdigit(): 
            return int(guess)
        else:
            print("Invalid input. Please enter a number.")



def get_high_low():
    while True:
        high_low = input("Do you think your number is higher or lower than the computer's? ").strip().lower()
        if high_low in ["higher", "lower"]:
            return high_low
        else:
            print("Invalid input. Please enter 'higher' or 'lower'.")



def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    round = 0
    score = 0
    while round < ROUNDS:
        print(f"Round {round + 1}")
        guess = get_guess()
        computer_guess = random.randint(1, 100)
        high_low = get_high_low()

        conditions = ( high_low == "higher" and guess > computer_guess) or (high_low == "lower" and guess < computer_guess)


        if conditions:
            print(f"You were right! The computer's number was {computer_guess}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_guess}")
            if score > 0:
               score -= 1
            print(f"Your score is now {score}")
        
        round += 1
    
    
    print("\n--------------------------------")
    print("Thanks for playing!")
    print(f"\nYour final score is {score} out of {ROUNDS}.")
    if score == ROUNDS:
        print("🟢🎉 Wow! You played perfectly!")
    elif score >= ROUNDS // 2:
        print("🟡 😊 Good job, you played really well!")
    else:
        print("🔴🙁 Better luck next time!")
    

        


if __name__ == "__main__":
    main()

