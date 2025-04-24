import random
import string
# password generator
print("Welcome to the password generator!")

# generate_password function
def generate_password():
    # define characters to choose from
    chars = string.ascii_letters + string.digits + string.punctuation
    # get number of passwords to generate
    number = int(input("Enter the number of passwords to generate: "))
    # get length of the password
    length = int(input("Enter the length of the password: "))

    print("\nHere are your passwords:")
    # generate passwords
    for p in range(number):
        password = ''
        for c in range(length):
            password += random.choice(chars)
        print(f"Password {p+1}: {password}")
    
# main function
def main():
    generate_password()

if __name__ == '__main__':
    main()
   


