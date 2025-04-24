def doubling(number: int) -> int:
    """
    Doubles the given number until it is less than 100.
    """
    # Double the number
    
    while number < 100:
        number = number * 2 # Update the current value by doubling it
        print(number, end=" ")  # Print on the same line with a space
    # Return the doubled number
    return number



def main():
    # ask number from user between 1 to 100
    ask_num = int(input("enter the between 1 to 100:"))
    doubling(ask_num)
if __name__ == '__main__':
    main()