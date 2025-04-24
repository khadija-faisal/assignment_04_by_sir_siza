

def greet(name : str):
    return "Assalam-u-Alaikum " + name + "! 😊"

def main():

    user_name : str = input("What is your name?: ")
    print(greet(user_name))
   

	
if __name__ == '__main__':
    main()