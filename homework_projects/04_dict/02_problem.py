
def get_user_phone_book():
    phone_book = {}
    while True:
        name = input("enter your name: ")
        if name == "":
            break

        number = input("enter your phone: ")
        if number == "" and not number.isdigit():
            print("phone number cannot be empty and must be numeric")
            continue
        phone_book[name] = number
    print(phone_book)
    return phone_book

def lookup_num(phone_book):
    while True:
        search_for_num = input("search name for number: ")
        if search_for_num == "":
            break
        if search_for_num in phone_book:
            print(f'{search_for_num} : {phone_book[search_for_num]}')

        else:
            print(search_for_num + "not in the phonebook")




def main():
    phone_book = get_user_phone_book()
    lookup_num(phone_book)




if __name__ == '__main__':
    main()