

def doubling(number: int) -> int:
    """
    Doubles the given number.
    """
    # Double the number
    number = number * 2
    # Return the doubled number
    return number

def main():
    """
    Main function that doubles the user's number.

    """
    # Get the user's number
    get_user_number = int(input("enter your number:"))
    # Call the doubling function and print the result
    print("your number doubled is: " + str(doubling(get_user_number)))
   
if __name__ == '__main__':
    main()