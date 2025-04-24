# Define the affirmation the user must type exactly (case-insensitive)
AFFIRMATION : str = "I am proud of how far I've come and excited for what's ahead."

def main():
      # Start an infinite loop to keep prompting the user until they type the correct affirmation
    while True:
         # Ask the user to type the affirmation
        user_motivation : str = input("Please type the following affirmation: "+ AFFIRMATION + "\n")
          # Check if the user input matches the affirmation (case-insensitive comparison)
        if user_motivation.lower() == AFFIRMATION.lower():
            print(user_motivation)
            print("that'ss my girl you can achieve your dream in Sha Allah very soon 💖")
            break
        else:  
            print("Hmmm... That was not the affirmation. Try again.\n")




# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()