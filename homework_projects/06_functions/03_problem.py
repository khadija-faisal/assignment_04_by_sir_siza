 


def get_int():
    """
    Gets integers from the user and returns a list of even numbers.
    """
    even_numbers: list[int] = []
      # Prompt the user for input
    get_int = input("Enter an integer: ")
    # Loop until the user enters an empty string
    while get_int != "":
        # Check if the number is even
        if int(get_int) % 2 == 0:
            # Add the number to the list
            even_numbers.append(int(get_int))
        # Prompt the user for input again
        get_int = input("Enter an integer: ")
    return even_numbers


def main():
    """
    Main function that gets even numbers from the user and prints them.
    """
    even_numbers_list = get_int()
    print(f"Even numbers: {even_numbers_list}")
    print(f"Count: {len(even_numbers_list)}")
  



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()