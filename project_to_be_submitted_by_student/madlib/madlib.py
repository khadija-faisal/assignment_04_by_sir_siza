
def madlib():

    print("Welcome to the Madlib Game!")
      # Ask the user to enter a time of day (e.g., "morning", "evening", "night")
    time_of_day = input("Time of Day: ")
    # Ask the user to enter a body part in plural form (e.g., "arms", "legs", "eyes")
    body_part_plural = input("Body Part (plural): ")
    # Ask the user to enter a color (e.g., "red", "blue", "green")
    color = input("Color: ")
    # Ask the user to enter a verb in past tense (e.g., "ran", "screamed", "jumped")
    verb_past_tense = input("Verb (past tense): ")
    # Ask the user to enter a food item (e.g., "pizza", "sushi", "ice cream")
    food = input("Food: ")
    # Ask the user to enter a noun (e.g., "house", "car", "book")
    noun1 = input("Noun: ")
    # Ask the user to enter a noun in plural form (e.g., "houses", "cars", "books")
    noun_plural_1 = input("Noun (plural): ")
    # Ask the user to enter an adjective (e.g., "happy", "sad", "funny")
    adj1 = input("Adjective: ")
    # Ask the user to enter an adjective (e.g., "happy", "sad", "funny")
    adj2 = input("Adjective: ")
    # Ask the user to enter an adjective (e.g., "happy", "sad", "funny")
    adj3 = input("Adjective: ")


    madlib = f"It was a {adj1} summer {time_of_day} when we realized that the vaccine to stop \
spread of the disease did not work. Instead, it produced ZOMBIES!!! They were thirsty for {body_part_plural} \
and the streets were lined with these monsters holding {noun_plural_1} in their hands. \
Their eyes were {color} with hunger as they {verb_past_tense} around the city looking for {food}. \
They were {adj2} and {adj3}, unknowing how to act in this human world... except eat {body_part_plural}!!!! \
That was their sole mission and they were dedicated towards achieving it for the sake of {noun1}."
    
    print(madlib)

def main():
    madlib()


if __name__ == "__main__":
    main()
