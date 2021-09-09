def fahrenheit_To_Celsius():
    f = input("Enter Degrees in Fahrenheit: ")
    c = (int(f) - 32) * (5/9)
    final_C = round(c, 2)
    print(f'The Degrees in Celsius is : {final_C}')


fahrenheit_To_Celsius()


def trapezoid_Area():
    print("Area of Trapezoid")
    height = float(input("Enter the height of the trapezoid: "))
    bottom = float(input("Enter the length of the bottom base: "))
    top = float(input("Enter the length of the top base: "))
    area = (0.5 * (top + bottom) * height)
    print(f'The area of the trapezoid is: {area}')


trapezoid_Area()


def angle_degrees_via_sides():
    print("This will tell you the degrees of each angle based\n on the number of sides in an equilateral shape")
    sides = int(input("How many sides on your shape? "))
    angle = (180 * (sides - 2)) / sides
    print(f'The degrees of each angle is {angle} degrees.')


angle_degrees_via_sides()
