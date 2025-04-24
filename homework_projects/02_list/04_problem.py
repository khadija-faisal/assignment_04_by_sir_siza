
# Problem Statement

# To see this in action, fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list. Don't return anything and see what happens! Compare this process to the x = change(x) example and note the differences.

def copies_add(my_list, data, num):
    my_list.extend([data for _ in range(num)])

def main():
   
   enter_text : str = input("enter a text to copy:")
   copies: int = int(input("enter number how many times to copy?:"))
   my_list : list[str] = []
   print("list before,", my_list)
   copies_add(my_list,enter_text,copies)
   
   print("list after",my_list)
                  




if __name__ == '__main__':
    main()