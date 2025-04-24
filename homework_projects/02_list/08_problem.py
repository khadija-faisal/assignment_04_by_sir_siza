# Set the maximum allowed number of elements in the list
MAX_LENGTH = 4
# Initialize an empty list to store user input
my_list = []
def get_text():
    """
    Prompts the user to enter their favorite fruits one by one.
    Continues until the user presses Enter without typing anything.
    Each entered fruit is added to the global list `my_list`.
    """
    fruits = input("enter your fav fruits name and press two time enter to stop:")
    while fruits != "":
        my_list.append(fruits)
        fruits = input("enter your fav fruits name and press two time enter to stop:")


def check_length():
    if len(my_list) == MAX_LENGTH:
        print(my_list)
    elif len(my_list) > MAX_LENGTH:
        while len(my_list) > MAX_LENGTH:
            my_list.pop()
        print(my_list)
    else:
        print("list is less then max length")
          

def main():
    get_text()
    check_length()


  
if __name__ == '__main__':
    main()