# PROBLEM

# In a file called grocery.py, implement a program that prompts 
# the user for items, one per line, until the user inputs control-d 
# (which is a common way of ending one’s input to a program). 
# Then output the user’s grocery list in all uppercase, sorted 
# alphabetically by item, prefixing each line with the number of 
# times the user inputted that item. No need to pluralize the 
# items. Treat the user’s input case-insensitively.

def main():
    grocery_list = {}

    while True:
        try:
            item = input().strip().upper()
            if item:
                grocery_list[item] = grocery_list.get(item, 0) + 1
        except EOFError:
            print()
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    sorted_items = sorted(grocery_list.keys())

    for item in sorted_items:
        print(f"{grocery_list[item]} {item}")

if __name__ == "__main__":
    main()
