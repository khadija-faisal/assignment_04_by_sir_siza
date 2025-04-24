
def sub_seven(n):
	n = n - 7
	return n


def main():
    num: int = int(input("Enter a number: "))
    num = sub_seven(num)
    print("the result is: ", num)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()