def main():
    user_input : float = float(input("Enter a number: "))
    if user_input == 0:
        print("print valid number")
    else:
        result : float = user_input ** 2
        print(f"The square of {user_input} is {result}.")
        
     



if __name__ == '__main__':
    main()