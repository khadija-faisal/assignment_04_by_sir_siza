


def get_name() -> str:
    """
    Gets the user's name and returns it.
    """
    # Get the user's name
    name = input("What is your name? ")
    # Return the user's name
    return name


def main():
    name = get_name() # get_name() will return a string which we store to the 'name' variable here
    print("Hello preetyyyy", name,"! 🥰🥰✨")

if __name__ == '__main__':
    main()