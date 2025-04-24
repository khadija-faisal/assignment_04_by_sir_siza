# problem 03
import math
def main():
   ab : float = float(input("Enter the length of side a to b in cm: "))
   ac : float = float(input("Enter the length of side b to c in cm: "))

   bc = math.sqrt(ab**2 + ac**2)
   # Display the work to the user
   print("a^2 + b^2 = c^2")
   print("a = " + str(ab) + " cm")
   print("b = " + str(ac) + " cm")
   print(f"c = {bc:.1f} cm")
   # Output the equivalent energy
   print(f"Hypotenuse = {bc:.1f} cm")
   

if __name__ == '__main__':
    main()

