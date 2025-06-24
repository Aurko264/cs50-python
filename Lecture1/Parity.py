# Basic 

""" x = int(input("What's is x: "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd") """

# Using function

def main():
    x = int(input("What's is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# Regular way

""" def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False """

# More efficient way 

def is_even(n):
    return n % 2 == 0
    
main()
