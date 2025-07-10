# PROBLEMS

# In a file called fuel.py, implement a program that prompts the 
# user for a fraction, formatted as X/Y, wherein each of X and Y 
# is a positive integer, and then outputs, as a percentage rounded 
# to the nearest integer, how much fuel is in the tank. If, though, 
# 1% or less remains, output E instead to indicate that the tank 
# is essentially empty. And if 99% or more remains, output F 
# instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y 
# is 0, instead prompt the user again. (It is not necessary for Y 
# to be 4.) Be sure to catch any exceptions like ValueError or 
# ZeroDivisionError.

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            gauge(percentage)
            break
        except ValueError:
            print("Invalid input. Please enter a fraction like X/Y where X and Y are integers.")
        except ZeroDivisionError:
            print("Invalid input. Y cannot be zero.")

def convert(fraction):
    x_str, y_str = fraction.split('/')

    x = int(x_str)
    y = int(y_str)

    if x < 0 or y < 0:
        raise ValueError("X and Y must be integers.")
    if x > y:
        raise ValueError("X cannot be greater than Y.")
    if y == 0:
        raise ZeroDivisionError("Y cannot  be zero.")

    percentage  = round((x / y) * 100)
    return percentage

def gauge(percentage):
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

if __name__ == "__main__":
    main()
