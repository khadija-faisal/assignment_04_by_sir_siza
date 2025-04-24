def main():
    
    degrees_fahrenheit = input("Enter temperature in Fahrenheit: ")
    degrees_fahrenheit = float(degrees_fahrenheit)
    degrees_celsius = (degrees_fahrenheit - 32) * 5 / 9
    print(f" Temperature: {degrees_fahrenheit}F = {degrees_celsius:.2f}C")





if __name__ == '__main__':
    main()