
def get_message():
    """
    Gets a message and a quantity from the user and prints the message that many times.
    """
    message = input("Enter a message: ")
    get_quantity = int(input("How many times to repeat your message: "))
    # Loop through the quantity
    for i in range(get_quantity):
        print(message)




def main():
    # Get the message and quantity from the user
    get_message()

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()