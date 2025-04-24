
#  problem 05
# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

def main():
   divendend : int = int(input("Enter the dividend: "))
   divior : int = int(input("Enter the divisor: "))
    # Perform the division and calculate the remainder
   result: int = divendend // divior
   remainder : int = divendend % divior
   print(f" In the result of the divison of {divendend} / {divior} is :....")
   print(f" {result} with a reminder of {remainder}")


if __name__ == '__main__':
    main()