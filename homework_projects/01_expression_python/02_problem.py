
# Problem 2: 
# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:
# E = m * c**2

def main():
     mass_value : float = float(input("Enter mass in kilograms: "))
     speed_of_light : float = 299792458  # Speed of light in m/s
     energy : float = mass_value * (speed_of_light**2)
      # Display work to the user
     print("e = m * C**2 = ")
     print("m = " + str(mass_value) + " kg")
     print("C = " + str(speed_of_light) + " m/s")

    # Output the equivalent energy

     print(f"Energy equivalent Joules : " + str(energy) + " J")

     



if __name__ == '__main__':
    main()







