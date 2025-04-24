def get_odd_and_even_numbers():
    """
    Prints whether numbers from 0 to 49 are even or odd.
    """
 
     # Loop through numbers from 0 to 49
    for i in range(50):
        # Check if the number is even
        if i % 2 == 0:
            print(f"{i} is even") # Print even message
        else:
            print(f"{i} is odd") # Print odd message



def main():
    get_odd_and_even_numbers()
   


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()