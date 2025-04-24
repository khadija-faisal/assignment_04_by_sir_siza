def main():
    list_of_num = []
    
    enter_num = input("enter numbers to add number in list and press enter to stop:  ")
    while enter_num != "" :
        list_of_num.append(enter_num)
        enter_num = input("enter numbers to add number in list and press enter to stop:  ")


    print(list_of_num)
        
    
if __name__ == '__main__':
    main()