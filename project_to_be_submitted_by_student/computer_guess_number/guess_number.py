import random 



def main():
    #print("welcome to the game of user guessing the number \nyou got 5 attempts to the number between 50 to 100")

    number_to_guess = random.randrange(50, 100)
    chances = 5 
    guess_counter = 0


    while guess_counter < chances:
        guess_counter += 1
        my_guess = int(input("enter your guess:"))

        if my_guess == number_to_guess:
            print(f"Wow! the number is {number_to_guess} and you found it right !! in the {guess_counter} attempt ")
            break
        elif guess_counter >= chances and my_guess != number_to_guess:
            print(f"Oops!, the number {number_to_guess} better luck next time")

        elif my_guess < number_to_guess:
            print("your guess is too low, try again")
        elif my_guess > number_to_guess:
            print("your guess is too high, try again")



if __name__ == "__main__":
    main()


