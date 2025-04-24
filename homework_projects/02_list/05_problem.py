
def first_elemnt(my_list):
    print(my_list[0])

def get_list():
    

    my_list = []
    ask_value: str = input("Please enter an element of the list or press enter to stop.:")
    while ask_value != "" :
        my_list.append(ask_value)
        ask_value = input("Please enter an element of the list or press two time enter to stop.:")
    return my_list


def main():
   my_list = get_list()
   first_elemnt(my_list)

   
if __name__ == '__main__':
    main()