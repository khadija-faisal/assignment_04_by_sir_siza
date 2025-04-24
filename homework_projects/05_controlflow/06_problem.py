def main():
    # ask number from user between 1 to 100
    ask_num = int(input("enter the between 1 to 100:"))
    while ask_num < 100:
        ask_num = ask_num * 2 # Update the current value by doubling it
        print(ask_num, end=" ")  # Print on the same line with a space
if __name__ == '__main__':
    main()