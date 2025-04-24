# Gravity constants for each planet relative to Earth's gravity
MERCURY = 0.376
VENUS = 0.889
MARS = 0.378
JUPITER = 2.36
SATURN = 1.081
URANUS = 0.815
NEPTUNE = 1.14


# Function to calculate planetary weight
# Multiplies Earth's weight with the gravity factor of the chosen planet
def planetary_weight_calculator(weight, planet_gravity):
    return weight * planet_gravity
    
# Function to get user input for planet name and return its gravity factor
def choose_planet():
    planet : str = input("Enter the name of the planet you want to calculate the weight on: ").strip().lower()
     # Return planet name and its gravity factor as a tuple
    if planet == "mercury":
        return "Mercury", MERCURY
    elif planet == "venus":
        return "Venus", VENUS
    elif planet == "mars":
        return "Mars", MARS
    elif planet == "jupiter":
        return "Jupiter", JUPITER
    elif planet == "saturn":
        return "Saturn", SATURN
    elif planet == "uranus":
        return "Uranus", URANUS
    elif planet == "neptune":
        return "Neptune", NEPTUNE
    else: 
        print("Invalid planet")
        return None, None
    


def main():
      # Prompt user for their weight on Earth
    weight = float(input("Enter your weight: "))

    planet_name, planet_gravity = choose_planet()
# Only calculate if a valid planet was chosen
    if planet_gravity is not None:
        calculated_weight = planetary_weight_calculator(weight, planet_gravity)
        print(f"you weight on {planet_name} is {round(calculated_weight, 2)}")
        print("Thank you for using the planetary weight calculator!")
    else:
        print("Invalid planet")

    

if __name__ == "__main__":
    main()


