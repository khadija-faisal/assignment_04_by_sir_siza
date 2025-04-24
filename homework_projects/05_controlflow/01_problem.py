import random 

 # Generate the secret number at random!
win_num =random.randint(0,40)
def main():
    
    while True:
          # Get user's guess
         guess_number = int(input(" Guess and enter a number between 0 to 39:"))   
         if guess_number == win_num :
             print("congratsssss !🎉🥳 you guess a right number " + str(guess_number))
             break
         elif guess_number > win_num : # if guess_number is greater then win_sum print guess is too high
             print("your guess is too high")
         else:
             print(" your guess is too low")
    

    

if __name__ == '__main__':
    main()