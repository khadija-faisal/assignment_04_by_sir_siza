MAXIMUM_HEIGHT = 50
def main():
    enter_your_height = input("enter your height: ")
    if enter_your_height >= MAXIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")





# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()