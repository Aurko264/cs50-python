# One way

"""i = 3
while i != 0:
    print("meow")
    i = i - 1"""

# Another way

"""i = 0
while i < 3:
    print("Meow")
    i += 1"""

# Another way

"""for i in [0, 1, 2]:
    print("meow")"""

# Another way 
"""
for i in range(3):
    print("meow")"""

# Another way

"""print("meow\n" * 3,end="")"""

# Another way

"""while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")"""

# Another way

"""def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("meow")

main()"""

# Another way

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print(meow)
    
main()