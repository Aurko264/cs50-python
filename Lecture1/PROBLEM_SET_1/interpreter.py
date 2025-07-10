# QUESTION 

# In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates 
# and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be
#  formatted as x y z, with one space between x and y and one space between y and z, wherein:

# x is an integer
# y is +, -, *, or /
# z is an intege

def main():
    expression = input("Expression: ")

    parts = expression.split(" ")

    x = int(parts[0])
    y = parts[1]
    z = int(parts[2])

    result = 0.0

    if y == "+":
        result = float(x + z)
    if y == "-":
        result = float(x - z)
    if y == "*":
        result = float(x * z)
    if y == "/":
        result = float(x / z)

    print(f"{result:.1f}")

if __name__ == "__main__":
    main()