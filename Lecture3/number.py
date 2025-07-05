# One way to handle exception

"""try:
     x = int(input("What's x? "))
     print(f"x is {x}")
except ValueError: # when the expected input is not given
     print("x is not an integer")"""

# Another way to handle it

"""try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else: # if every thing goes well in "try" without an error than 
      #it will print "else".
    print(f"x is {x}")"""

# Making it more user friendly

"""while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")"""

# Creating a function

"""def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")

main()"""

# Pass

def main():
    x = get_int("What's x?")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()