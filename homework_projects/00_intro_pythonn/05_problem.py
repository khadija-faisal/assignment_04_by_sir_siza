def main():

    triangle_side_1 : float = input("Enter the length of the first side of the triangle: ")
    triangle_side_2 : float = input("Enter the length of the second side of the triangle: ")
    triangle_side_3 : float = input("Enter the length of the third side of the triangle: ")
    triangle_side_1 = float(triangle_side_1)
    triangle_side_2 = float(triangle_side_2)
    triangle_side_3 = float(triangle_side_3)
    result = triangle_side_1 + triangle_side_2 + triangle_side_3
    if result > 180:
        print("The triangle is not valid.")
    elif result == 180:
        print("The triangle is valid.")
    else:
        print("The triangle is not valid.")
    print(f"The sum of the angles is {result} degrees.")



if __name__ == '__main__':
    main()