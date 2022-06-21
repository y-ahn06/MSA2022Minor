from cmath import pi
import math


def get_float_value(prompt):
    run_again = True
    while (run_again):
        try:
            user_input = float(input(prompt))
            if(user_input <= 0):
                print("ERROR: Value must be greater than 0.\n")
                continue
        except:
            print("ERROR: Input must be a number.\n")
        else:
            run_again = False

    return user_input

loop = true
while (loop)
radius = get_float_value("Radius of cylinder: ")
height = get_float_value("Height of cylinder: ")
total_volume = (3.14159) * 2 * radius * height
print(f"The area of the cylinder is {total_volume}")

