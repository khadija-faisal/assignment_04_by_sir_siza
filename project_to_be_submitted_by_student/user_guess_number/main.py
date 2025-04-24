import random
# computer guess the number
def computer_guess(x):
    # computer guess the number between 1 and x
    low = 1
    high = x
    # feedback from the user
    feedback = ''
    while feedback != 'c' :
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'is {guess} too high (H), too low (L), or correct (C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'yay! the computer guessed your number, {guess}, correctly! 🎉🎉')


def main():
    computer_guess(100)


if __name__ == "__main__":
    main()

    


