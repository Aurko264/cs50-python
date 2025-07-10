# QUESTION

# In a file called camel.py, implement a program that prompts the
# user for the name of a variable in camel case and outputs the 
# corresponding name in snake case. Assume that the user’s input 
# will indeed be in camel case.


def main():
    camel_case = input("camelCase: ")
    snake_case = convert_snakecase(camel_case)
    print("Snake_case:", snake_case)

def convert_snakecase(camel_case):
    snakecase_name = ""
    for char in camel_case:
        if char.isupper():
            snakecase_name += "_" + char.lower()
        else:
            snakecase_name += char

    if snakecase_name.startswith("_"):
            snakecase_name = snakecase_name[1:]

    return snakecase_name

if __name__ == "__main__":
    main()