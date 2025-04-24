 
def main():
    num_list: list[int] = [1,3,5,7,9,10,12,15]
    num_list = [num * 2 for num in num_list]
    print(num_list)

    
if __name__ == '__main__':
    main()