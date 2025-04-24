MAX_LENGTH = 10000 # Set the maximum length of the Fibonacci sequence to print

def main():
    first_num = 0 # Initialize the first number of the Fibonacci sequence
    second_num = 1 # Initialize the second number of the Fibonacci sequence
    # Print the first two numbers manually
    print(first_num, second_num, end=" ")

        # Start the loop from the 3rd Fibonacci number (index 2) and continue until MAX_LENGTH
    for i in range(MAX_LENGTH):
        fab = ( first_num + second_num)
        first_num = second_num
        second_num = fab
        print(fab, end=" ")
  
        


    
if __name__ == '__main__':
    main()