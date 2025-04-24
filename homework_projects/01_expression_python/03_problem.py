#problem 3
#Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

def main():
    # Get the number of feet from the user
    feet_value : float = float(input("Enter length in feet: "))

    # Convert feet to inches
    inches_value : float = feet_value * 12

    # Display the result
    print(f"{feet_value} feet is equal to {inches_value:.1f} inches.")
    
if __name__ == '__main__':
    main()