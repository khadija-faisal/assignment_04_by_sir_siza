# List containing user information
user_info : list[str] = ["Khadijah", "20", "khadija@gmail.com", "43.2" , "web developer"]


# Function to access an item from the list based on index
def accessing_list():
      ask_index = int(input("enter a index number:"))
      if 0 <= ask_index < len(user_info):
           return user_info[ask_index]
      else:
            print("invalid index number")
            return None


# Function to add an item to the list
def add_item():
      while True:
        ask_item = input("enter a item:")
        if ask_item == "":
            print("item can't be empty")
            
        else:
            user_info.append(ask_item)
            print("Updated list:", user_info)
            return f"'{ask_item}' added to the list!"


# Function to slice an item from the list based on index
def slice_item():
      ask_start_index = int(input("enter a start index number:"))
      ask_end_index = int(input("enter a end index number:"))
      if ask_start_index > ask_end_index:
            print("start index can't be greater than end index")
      else:
            slice_value = user_info[ask_start_index:ask_end_index]
            return slice_value


# Main function to run the program
def main():
      # Welcome message
      print("welcome to the list program")
      print("1. Accessing list")
      print("2. Add item")
      print("3. Slice item")
      print("4. Exit")
      # Loop to handle user input
      while True:
        try:
            ask_choice = int(input("Enter your choice: "))
            # Conditional statements to handle user choice
            if ask_choice == 1: # Accessing list
                print(accessing_list())
            elif ask_choice == 2: # Add item
                print(add_item())
            elif ask_choice == 3: # Slice item
                print(slice_item())
            elif ask_choice == 4: # Exit  
                break
            else:
                print("invalid choice")
        except ValueError:
            print("Invalid input. Please enter a number.")
        continue  
       

if __name__ == "__main__":
      main()

     
     
            

                   

                   

    










