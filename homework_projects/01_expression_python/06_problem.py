#problem 6
import random
#Simulate rolling two dice, and prints results of each roll as well as the total.

dice = 6
def main():
    deice_1 = random.randint(1, dice)
    deice_2 = random.randint(1, dice)
    total = deice_1 + deice_2
    print("Dice 1: ", deice_1)
    print("Dice 2: ", deice_2)
    print("Total: ", total)
    if total == 2:
        print("Snake Eyes!")
    elif total == 12:
        print("Box Cars!")
    elif total == 7:
        print("Lucky 7!")
    elif total == 11:
        print("Yo!")
    else:
        print("No special rolls.")
    print("Roll again? (y/n)")
    again = input()
    if again.lower() == 'y':
        main()
    else:
        print("Goodbye!")



if __name__ == "__main__":
    main()