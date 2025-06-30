"""def main():
    print_column(3)

#def print_column(height):
#    for _ in range(height):
#        print("#")

# Another way

def print_column(height):
    print("#\n" * height, end="")

main()"""

# Printing in row

"""def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()"""

# Printing square

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
#       for j in range(size):
#           print("#", end="")
#        print()

# Another way to write the "j" loop

        print("#" * size)

main()