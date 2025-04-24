import random
# problem 1
#Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

dice  = 6

def roll_dice():
    # Simulate rolling two dice, three times
    # Prints the results of each die roll

    for i in range(3): 
        diece_1 = random.randint(1, dice)
        diece_2 = random.randint(1, dice)
        
        # Print the results of each die roll
        print(f'Roll {i+1}: {diece_1} and {diece_2}')
def main():
    # Variable scope demonstration
       
    diece_1 = 12
    diece_2 = 15
    print(f'before calling the function roll_dice(), {diece_1} and {diece_2}')

    roll_dice()
    roll_dice()
    roll_dice()
    # Print the values of diece_1 and diece_2 after the function call
    print(f'after calling the function roll_dice(), {diece_1} and {diece_2}')

    



if __name__ == '__main__':
    main()