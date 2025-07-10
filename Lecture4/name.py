import sys

# One way to write it.

"""try:
    print("hello, my name is" , sys.argv[1])
except IndexError:
    print("Too few arguments")"""

# Another way to write it

"""if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
     print("hello, my name is", sys.argv[1])"""

# Another way to write it

"""if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("To many arguments")
else:
    print("hello, my name is", sys.argv[1])"""

# Another way to write if user want multiple names.

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]: # if we add [1: "-1"]  we slice from end of the list
        # or iterate over it.
    print("hello, my name is", arg)