def take_average():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    sum = a + b
    average = sum / 2
    return average 


def main():
    average_of_two_numbers = take_average()
    average_of_two_numbers1 = take_average()
    print(f"The average of the two numbers is {average_of_two_numbers}")
    print(f"The average of the two numbers is {average_of_two_numbers1}")

    

      
    
if __name__ == '__main__':
    main()