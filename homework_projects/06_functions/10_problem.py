def print_ones_digit(num): 

    print("The ones digit is", num % 10)

def main():
    get_num = int(input("Enter a number: "))
    print_ones_digit(get_num)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()