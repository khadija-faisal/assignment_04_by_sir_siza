

def in_range(num : int, lower : int, upper : int):

    if num >= lower and num <= upper:
        return True
    else:
        return False


def main():

    get_user_number : int = int(input("Enter a number: "))
    get_lower_number : int = int(input("Enter a lower bound: "))
    get_upper_number : int = int(input("Enter a upper bound: "))
    print(in_range(get_user_number, get_lower_number, get_upper_number))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()