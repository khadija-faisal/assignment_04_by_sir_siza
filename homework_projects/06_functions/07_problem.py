

def get_divisor(num):
    """
    Prints all divisors of a given number.
    """
    for i in range(1,num+1):
        # Check if i is a divisor of num
        if num % i == 0:
            # Print the divisor
            print(f"{i} is a divisor of {num}")
 


def main():
    """
    Main function that gets a number from the user and prints its divisors.
    """
    # Get the number from the user
    num = int(input("Enter a number: "))
    get_divisor(num)
    
    

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()