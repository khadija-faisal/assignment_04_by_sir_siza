import random




PROMPT: str = "What do you want? " # The prompt for the user to input their request
JOKE: list[str] = ["Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'","I don't need a hairdresser, I just need a good git reset","Why was the developer always calm? He knew how to handle exceptions."]

SORRY: str = "Sorry I only tell jokes." # The message that the program will print if the user inputs something other than "joke"

def main():
    print(PROMPT)

    # Get the user's input and convert it to lowercase
    user_input: str = input().strip().lower()

    # If the user inputs "joke", print a random joke
    if user_input == "joke":
        print(random.choice(JOKE))
    else:
        print(SORRY)

if __name__ == "__main__":
    main()
