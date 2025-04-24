
def get_user_info():
    # Input for name
    name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
     
    # Input for email with validation
    while True:
        email = input("Enter your email: ")
        if "@" in email and "." in email:
            break
        else:
            print("Invalid email. Please enter a valid email address.")

    return name, last_name, email


def main():
    user_data = get_user_info()
    print("Received the following user data:", user_data)

if __name__ == "__main__":
     main()