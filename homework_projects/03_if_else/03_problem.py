def main():

       # Ask the user to input a year
    enter_year = input("please input a year ")

      # Check if it's a leap year using the official rule:
    # Divisible by 4 and not divisible by 100, unless divisible by 400
    if (enter_year % 4 == 0 and enter_year % 100 != 0) or (enter_year % 400 == 0):
        print("That's a leap year!")

    else: 
        print("That's not a leap year.")



if __name__ == '__main__':
    main()